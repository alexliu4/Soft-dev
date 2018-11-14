# Alex Liu
# SoftDev1 pd7
# K24 -- A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib.request
import json
import ssl
app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.nasa.gov/planetary/apod?api_key=xygyAxeGinPW9YBcPBX01p9Aba9lXfhrAh5O5WX5"
    context = ssl._create_unverified_context()
    v = urllib.request.urlopen(url, context=context)
    print(v)

    response = v.read()
    print(response)

    data = json.loads( response )
    print (data)

    return render_template("template.html", pic=data['url'], explanation=data['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
