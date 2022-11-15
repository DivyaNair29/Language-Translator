#!/usr/bin/env python
# coding: utf-8

# In[20]:


from flask import Flask, request, url_for, redirect, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        try:
            text_to_translate = request.form["text-to-translate"].lower()
            language = request.form["select-language"]
            translated_text = translator.translate(text_to_translate, dest=language)
            text = translated_text.text
        except:
            text = "{ERROR: We are not able to handle your request right now}"
        return render_template('index.html', translation_result=text)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

