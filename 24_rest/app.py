# RayMond -- Alex Liu, Ray Onishi
# SoftDev1 pd7
# K24 -- A RESTful Journey Skyward
# 2018-11-13 F

import urllib
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    v = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=uoaMLMJCuYOsCiK0kN6sxe8zUxVBwNWmuOdMA30D")
    print(v)
    # response = u.read()
    # data = json.loads( response )
    return render_template("template.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
