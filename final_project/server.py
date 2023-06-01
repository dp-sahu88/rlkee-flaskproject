from machinetranslation.translator import  englishToFrench, frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToSpanish",methods = ['POST', 'GET'])
def english2French():
    textToTranslate = request.args.get('textToTranslate')
    print (textToTranslate)
    french_text = englishToFrench(textToTranslate)
    return french_text

@app.route("/spanishToEnglish",methods = ['POST', 'GET'])
def french2English():
    textToTranslate = request.args.get('textToTranslate')
    print (textToTranslate)
    french_text = frenchToEnglish(textToTranslate)
    return french_text

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)