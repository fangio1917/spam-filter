import gradio as gr

def show(spam):
    if spam == 'this not spam':
        result = False
    else:
        result = True

    return result, 0.91

demo = gr.Interface(
    fn=show, 
    inputs=gr.Textbox(label="spam email context"), 
    outputs=[
        gr.Text(label="result"),
        gr.Number(label="sorce")
    ]
)
demo.launch(share=False)
