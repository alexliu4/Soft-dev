# Alex Liu
# SoftDev1 pd7
# K25 -- Getting more REST
# 2018-11-13

from flask import Flask, render_template
import urllib.request
import json
import ssl
app = Flask(__name__)

@app.route('/')
def home():
    print("==============================================")
    url = "https://api.got.show/api/characters/locations"
    context = ssl._create_unverified_context()
    print("=============" + url + "=============")
    v = urllib.request.urlopen(url, context=context)
    print(v)

    response = v.read()
    print(response)

    data = json.loads( response )
    print (data)

    return render_template("template.html", name=data[0]['name'], location=data[0]['locations'])


if __name__ == "__main__":
    app.debug = True
    app.run()
