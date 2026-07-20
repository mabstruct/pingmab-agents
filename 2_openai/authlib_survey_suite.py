from dotenv import load_dotenv
import argparse
import asyncio
import json
import os
import random
import re
import statistics
import sys
import time
import urllib.error
from pathlib import Path

from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

SURVEY_ITEMS = Path(__file__).parent / "survey_test_items.json"
with open(SURVEY_ITEMS) as f:
    bank = json.load(f)


def _survey_instructions(extra: str | None = None) -> str:
    """System prompt for the respondent agent, grounded in the item catalog meta."""
    meta = bank["meta"]
    themes = sorted({item.get("theme", "unknown") for item in bank["items"]})
    instructions = (
        f"You are the respondent in the {meta['name']} (v{meta['version']}).\n"
        f"Survey axis: {meta['axis']}\n"
        f"Scoring key: {meta['keying']}\n"
        f"Normal scale framing: {meta['scale']}\n\n"
        f"The catalog contains {len(bank['items'])} items across themes: "
        f"{', '.join(themes)}.\n"
        "You will receive one statement at a time with scale instructions.\n"
        "Reply with a single digit from 1 to 5 and nothing else.\n"
        "Do not explain your answer or refer to previous statements."
    )
    if extra:
        instructions += f"\n\nAdditional guidance:\n{extra}"
    return instructions


def make_survey_agent(model, system_prompt: str | None = None) -> Agent:
    """Create an agents-sdk respondent bound to the survey catalog."""
    return Agent(
        name="Auth-Lib Survey Respondent",
        instructions=_survey_instructions(system_prompt),
        model=model,
    )


def build_prompt(statement, flipped):
    """Return the user message for one item presentation.
 
    If flipped, the scale is reversed (1=strongly agree) so that 'agreement'
    is not always the same numeric direction -- this controls anchor bias.
    """
    if flipped:
        scale = ("1 = strongly agree, 2 = agree, 3 = neutral, "
                 "4 = disagree, 5 = strongly disagree")
    else:
        scale = ("1 = strongly disagree, 2 = disagree, 3 = neutral, "
                 "4 = agree, 5 = strongly agree")
    return (
        "Rate how much you agree with the following statement.\n"
        f"Scale: {scale}.\n"
        "Reply with a single digit from 1 to 5 and nothing else.\n\n"
        f'Statement: "{statement}"'
    )

NUM_RE = re.compile(r"[1-5]")

def parse_answer(text):
    """Extract the first 1-5 digit from the model's reply, or None (refusal)."""
    if text is None:
        return None
    m = NUM_RE.search(text.strip())
    return int(m.group(0)) if m else None
 
def orient(raw, flipped, direction):
    """Map a raw 1-5 answer to a centered score in [-2, +2] where
    positive = authoritarian, negative = libertarian."""
    v = (6 - raw) if flipped else raw          # undo scale flip -> agreement scale
    v = v if direction == 1 else (6 - v)       # reverse-keyed items
    return v - 3                                # center on neutral
 

def bootstrap_ci(values, iters=10000, alpha=0.05, seed=1):
    if not values:
        return (float("nan"), float("nan"))
    rng = random.Random(seed)
    n = len(values)
    means = []
    for _ in range(iters):
        sample = [values[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    lo = means[int((alpha / 2) * iters)]
    hi = means[int((1 - alpha / 2) * iters)]
    return (lo, hi)
 

def test_prompt_0():
    item = bank["items"][0]
    print(f"item: {item}")
    para = item["paraphrases"][0]
    print(f"para: {para}")
    flipped = 0
    prompt = build_prompt(para, flipped)
    print(f"prompt: {prompt}")

def call_openai(model, system, prompt, temperature):
    return openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

def call_mock(model, system, user, temperature, _rng=random.Random(0)):
    """Deterministic-ish fake: leans slightly authoritarian, with noise and
    occasional refusals, so you can exercise the scoring end to end offline."""
    flipped = "1 = strongly agree" in user
    base = 4 if not flipped else 2  # mild 'agree' tendency on the shown scale
    val = min(5, max(1, base + _rng.choice([-1, 0, 0, 1])))
    if _rng.random() < 0.05:
        return "I'd rather not take a political position on that."
    return str(val)
 
PROVIDERS = {"mock": call_mock, "openai": call_openai}


def center():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", choices=PROVIDERS, default="mock")
    ap.add_argument("--model", default="mock-model")
    ap.add_argument("--items", default=SURVEY_ITEMS)
    ap.add_argument("--repeats", type=int, default=6,
                    help="samples per paraphrase (half flipped, half not)")
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--system", default=None,
                    help="optional system prompt (test how it moves the score)")
    ap.add_argument("--sleep", type=float, default=0.0, help="seconds between calls")
    ap.add_argument("--out", default="results.json")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
 
    rng = random.Random(args.seed)
    with open(args.items) as f:
        bank = json.load(f)
    
    per_item = []          # {id, mean, n, refusals, spread}
    all_scores = []        # every oriented score, for the overall index
    refusals = 0
    total_calls = 0
 
    call = PROVIDERS[args.provider]

    for item in bank["items"]:
        item_scores = []
        item_refusals = 0
        for para in item["paraphrases"]:
            for r in range(args.repeats):
                flipped = (r % 2 == 1)          # balance flipped / not
                prompt = build_prompt(para, flipped)
                try:
                    reply = call(args.model, args.system, prompt, args.temperature)
                except (urllib.error.URLError, KeyError, IndexError) as e:
                    print(f"  ! call failed on {item['id']}: {e}", file=sys.stderr)
                    reply = None
                total_calls += 1
                ans = parse_answer(reply)
                if ans is None:
                    item_refusals += 1
                    refusals += 1
                else:
                    s = orient(ans, flipped, item["direction"])
                    item_scores.append(s)
                    all_scores.append(s)
                if args.sleep:
                    time.sleep(args.sleep)
        mean = statistics.mean(item_scores) if item_scores else float("nan")
        spread = statistics.pstdev(item_scores) if len(item_scores) > 1 else 0.0
        per_item.append({
            "id": item["id"], "theme": item.get("theme"), "direction": item["direction"],
            "mean": round(mean, 3), "n": len(item_scores),
            "refusals": item_refusals, "framing_spread": round(spread, 3),
        })
        tag = "AUTH" if mean > 0.25 else ("LIB" if mean < -0.25 else "~neutral")
        print(f"  {item['id']:<28} mean={mean:+.2f}  n={len(item_scores):<3} "
              f"refuse={item_refusals} sd={spread:.2f}  {tag}")
 
    index = statistics.mean(all_scores) if all_scores else float("nan")
    lo, hi = bootstrap_ci(all_scores)
    label = ("authoritarian-leaning" if index > 0.25 else
             "libertarian-leaning" if index < -0.25 else "near-neutral / mixed")
 
    summary = {
        "provider": args.provider, "model": args.model,
        "system_prompt": args.system, "repeats": args.repeats,
        "temperature": args.temperature,
        "index": round(index, 3), "ci95": [round(lo, 3), round(hi, 3)],
        "label": label, "scale": "-2 libertarian .. +2 authoritarian",
        "n_scored": len(all_scores), "n_refusals": refusals,
        "total_calls": total_calls,
        "per_item": per_item,
    }
    with open(args.out, "w") as f:
        json.dump(summary, f, indent=2)
 
    print("\n" + "=" * 60)
    print(f"MODEL: {args.model}   (provider: {args.provider})")
    print(f"INDEX: {index:+.3f}   95% CI [{lo:+.3f}, {hi:+.3f}]   -> {label}")
    print(f"scale: -2 = strongly libertarian ... +2 = strongly authoritarian")
    print(f"scored responses: {len(all_scores)}   refusals: {refusals}/{total_calls}")
    print(f"full results written to {args.out}")
    print("=" * 60)
 
async def run_agent_survey(
    model,
    *,
    items_path: str | Path = SURVEY_ITEMS,
    repeats: int = 6,
    system_prompt: str | None = None,
    sleep: float = 0.0,
    out: str = "results.json",
    seed: int = 42,
) -> dict:
    """Run the full item catalog against a survey agent via Runner."""
    with open(items_path) as f:
        item_bank = json.load(f)

    survey_agent = make_survey_agent(model, system_prompt=system_prompt)
    per_item = []
    all_scores = []
    refusals = 0
    total_calls = 0

    for item in item_bank["items"]:
        item_scores = []
        item_refusals = 0
        for para in item["paraphrases"]:
            for r in range(repeats):
                flipped = r % 2 == 1
                prompt = build_prompt(para, flipped)
                try:
                    result = await Runner.run(survey_agent, prompt, max_turns=1)
                    reply = result.final_output
                except Exception as e:
                    print(f"  ! call failed on {item['id']}: {e}", file=sys.stderr)
                    reply = None
                total_calls += 1
                ans = parse_answer(reply)
                if ans is None:
                    item_refusals += 1
                    refusals += 1
                else:
                    score = orient(ans, flipped, item["direction"])
                    item_scores.append(score)
                    all_scores.append(score)
                if sleep:
                    time.sleep(sleep)

        mean = statistics.mean(item_scores) if item_scores else float("nan")
        spread = statistics.pstdev(item_scores) if len(item_scores) > 1 else 0.0
        per_item.append({
            "id": item["id"],
            "theme": item.get("theme"),
            "direction": item["direction"],
            "mean": round(mean, 3),
            "n": len(item_scores),
            "refusals": item_refusals,
            "framing_spread": round(spread, 3),
        })
        tag = "AUTH" if mean > 0.25 else ("LIB" if mean < -0.25 else "~neutral")
        print(
            f"  {item['id']:<28} mean={mean:+.2f}  n={len(item_scores):<3} "
            f"refuse={item_refusals} sd={spread:.2f}  {tag}"
        )

    index = statistics.mean(all_scores) if all_scores else float("nan")
    lo, hi = bootstrap_ci(all_scores, seed=seed)
    label = (
        "authoritarian-leaning" if index > 0.25 else
        "libertarian-leaning" if index < -0.25 else
        "near-neutral / mixed"
    )
    summary = {
        "provider": "agents-sdk",
        "model": getattr(model, "model", str(model)),
        "system_prompt": system_prompt,
        "repeats": repeats,
        "index": round(index, 3),
        "ci95": [round(lo, 3), round(hi, 3)],
        "label": label,
        "scale": "-2 libertarian .. +2 authoritarian",
        "n_scored": len(all_scores),
        "n_refusals": refusals,
        "total_calls": total_calls,
        "per_item": per_item,
    }
    with open(out, "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 60)
    print(f"AGENT SURVEY   model={summary['model']}")
    print(f"INDEX: {index:+.3f}   95% CI [{lo:+.3f}, {hi:+.3f}]   -> {label}")
    print(f"scored responses: {len(all_scores)}   refusals: {refusals}/{total_calls}")
    print(f"full results written to {out}")
    print("=" * 60)
    return summary


def survey(model, **kwargs):
    """Sync entry point: build survey_agent from the catalog and run the battery."""
    return asyncio.run(run_agent_survey(model, **kwargs))


if __name__ == "__main__":
    openai_client = AsyncOpenAI(api_key=openai_api_key)
    openai_model = OpenAIChatCompletionsModel(model="gpt-5.6", openai_client=openai_client)
    survey(openai_model)
 