from pyscript import document
import enc
import dec


def encr(event):
    output = document.querySelector("#output")
    out = dec.e()
    output.innerText = out
def dcr(event):
    texts = document.querySelector("#enq")
    text = texts.value
    enc.e(text)