import gradio as gr
import re
import matplotlib
matplotlib.use('Agg') # biar dia gak nampilin window baru kalo visualisasi
import matplotlib.pyplot as plt

def _count_vocal(s):
    s.lower()
    list_vocal = ['a', 'i', 'u', 'e', 'o']
    total_char = []
    for vocal in list_vocal:
        total_char.append(s.count(vocal))

    fig = plt.figure()
    plt.bar(list_vocal, total_char)
    plt.title("Jumlah huruf vokal")
    plt.xlabel("Huruf vokal")
    plt.ylabel("Jumlah")
    return fig


def _remove_punct(s):
    fig = _count_vocal(s)
    return re.sub(r"[^\w\d\s]+", "",s), fig

gradio_ui = gr.Interface(
    fn=_remove_punct,
    title="simple interface",
    inputs=[gr.Textbox(label = "input text")],
    outputs=[gr.Textbox(label = "output text"), gr.Plot()] # 2 output ngikut yang dari return di _remove_punct
)

gradio_ui.launch()