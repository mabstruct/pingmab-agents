import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from styles_mab import CSS, JS, EXAMPLES, HEADER_HTML

load_dotenv(override=True)


async def run(query: str):
    async for status_update in ResearchManager().run(query):
        yield status_update


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            placeholder="Type a research question...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Investigate", variant="primary", elem_id="dr-run", scale=1)

    gr.HTML('<div class="dr-examples-label">Try one</div>')
    gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    report = gr.Markdown(elem_id="dr-report")

    run_button.click(run, inputs=query_textbox, outputs=report)
    query_textbox.submit(run, inputs=query_textbox, outputs=report)


MAB_THEME = (
    gr.themes.Base(primary_hue=gr.themes.colors.cyan)
    .set(
        body_background_fill="transparent",
        body_background_fill_dark="transparent",
        block_background_fill="transparent",
        block_background_fill_dark="transparent",
        body_text_color="rgba(255, 255, 255, 0.88)",
        body_text_color_dark="rgba(255, 255, 255, 0.88)",
        block_label_text_color="rgba(255, 255, 255, 0.68)",
        block_label_text_color_dark="rgba(255, 255, 255, 0.68)",
    )
)


if __name__ == "__main__":
    ui.launch(css=CSS, js=JS, theme=MAB_THEME)
