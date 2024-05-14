import gradio as gr
from model_vit import result_vit
from model_bert import result_bert
from model_cat import result_cat

vit = gr.Interface(fn=result_vit, inputs=gr.Image(type="numpy"),
                   outputs=[gr.Number(label="допустимое", precision=5),
                            gr.Number(label="недопустимое", precision=5)])

bert = gr.Interface(fn=result_bert, inputs=gr.Image(type="numpy"),
                    outputs=[gr.Textbox(label="распознанный текст", lines=3),
                             gr.Number(label="допустимое", precision=5),
                             gr.Number(label="недопустимое", precision=5)])

pipe = gr.Interface(fn=result_cat, inputs=gr.Image(type="numpy"),
                    outputs=[gr.Number(label="допустимое", precision=5),
                             gr.Number(label="недопустимое", precision=5),
                             gr.Textbox(label="предсказанный класс", lines=1)])

app = gr.TabbedInterface(interface_list=[vit, bert, pipe],
                         tab_names=["ViT predictions", "Bert predictions", "My Pipeline predictions"])

app.launch()
