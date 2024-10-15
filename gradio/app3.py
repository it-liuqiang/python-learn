import gradio as gr

def change_textbox(choice):
    if choice == "short":
        return gr.Textbox(lines=2, visible=True)
    elif choice == "long":
        return gr.Textbox(lines=8, visible=True, value="Lorem ipsum dolor sit amet")
    else:
        return gr.Textbox(visible=False)

with gr.Blocks() as demo:
    radio = gr.Radio(
        ["short", "long", "none"], label="What kind of essay would you like to write?",value="none"
    )
    text = gr.Textbox(lines=2, interactive=True, show_copy_button=True,visible=False)
    radio.change(fn=change_textbox, inputs=radio, outputs=text)

demo.launch()
