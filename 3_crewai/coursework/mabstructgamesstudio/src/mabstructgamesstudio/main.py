#!/usr/bin/env python
import sys
import warnings

from mabstructgamesstudio.crew import Mabstructgamesstudio

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    #print("Enter the game title: ")
    game_title = input("Enter the game title: ")
    inputs = {
        'game_title': game_title
    }

    try:
        Mabstructgamesstudio().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "game_title": "Space Miners",
    }
    try:
        Mabstructgamesstudio().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    Optional second argument: game_title (e.g. "The Big Swallow").
    """
    import os

    from mabstructgamesstudio.tools.game_context import (
        load_persisted_game_title,
        resolve_game_title,
        set_game_title,
    )

    try:
        task_id = sys.argv[1]
        inputs = None

        if len(sys.argv) > 2:
            inputs = {"game_title": sys.argv[2]}
        elif os.getenv("GAME_TITLE"):
            inputs = {"game_title": os.environ["GAME_TITLE"]}
        else:
            persisted = load_persisted_game_title()
            if persisted:
                inputs = {"game_title": persisted}

        if inputs and inputs.get("game_title"):
            set_game_title(str(inputs["game_title"]))
        else:
            resolve_game_title()

        Mabstructgamesstudio().crew().replay(task_id=task_id, inputs=inputs)

    except ValueError as e:
        if "not found in the crew's tasks" in str(e):
            raise Exception(
                f"{e}\n\nThat task ID is from an older run. "
                "List current IDs with: crewai log-tasks-outputs\n"
                'Deploy without replay: uv run deploy_game "The Big Swallow"'
            ) from e
        raise Exception(f"An error occurred while replaying the crew: {e}") from e
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}") from e


def deploy_game():
    """
    Run tests, check the deployment gate, and publish to here.now.
    Usage: deploy_game ["The Big Swallow"]
    """
    import os

    from mabstructgamesstudio.tools.game_context import (
        require_game_title,
        resolve_game_title,
        set_game_title,
    )
    from mabstructgamesstudio.tools.here_now_tool import deploy_to_here_now
    from mabstructgamesstudio.tools.telegram_tool import send_telegram_message
    from mabstructgamesstudio.tools.test_game_tool import (
        check_deployment_gate,
        run_game_tests,
    )

    try:
        if len(sys.argv) > 1:
            set_game_title(sys.argv[1])
        elif os.getenv("GAME_TITLE"):
            set_game_title(os.environ["GAME_TITLE"])
        elif not resolve_game_title():
            raise Exception(
                'Provide a game title: uv run deploy_game "The Big Swallow"'
            )

        title = require_game_title()
        print(f"Game: {title}")
        print(run_game_tests.run())
        gate = check_deployment_gate.run()
        print(gate)
        if not gate.startswith("DEPLOY ALLOWED"):
            raise Exception("Deployment gate is blocked.")

        artifact = f"output/{title}/index.html"
        deploy_result = deploy_to_here_now.run(
            artifact_path=artifact,
            game_title=title,
        )
        print(deploy_result)

        if deploy_result.startswith("Deployed to"):
            site_url = deploy_result.splitlines()[0].replace("Deployed to ", "").strip()
            message = (
                f"{title} playtest build is ready: {site_url}\n"
                "Gate: pass. Temporary here.now site."
            )
            print(send_telegram_message.run(message=message))
    except Exception as e:
        raise Exception(f"An error occurred while deploying the game: {e}") from e


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "game_title": "Space Miners",
    }

    try:
        Mabstructgamesstudio().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "game_title": "",
    }

    try:
        result = Mabstructgamesstudio().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
