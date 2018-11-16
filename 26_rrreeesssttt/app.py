# Alex Liu
# SoftDev1 pd7
# K26 -- A RESTful Journey Skyward
# 2018-11-15

import urllib.request
import json
import ssl

from flask import Flask, render_template

app = Flask(__name__)

print("============================================================")
apikey = "30370a68e63546a520f00a0640a999ac0e911cad"
url1 = "https://www.calendarindex.com/api/v1/holidays?country=US&year=2018&state=NY&api_key=" #url for new york
context = ssl._create_unverified_context()
# print("=============" + url1 + "=============\n\n")
user_agent = "Mozilla"
headers = {'User-Agent': user_agent, }

@app.route('/')
def home():
    # First API: Calender
    request = urllib.request.Request(url1 + apikey, None, headers)
    v = urllib.request.urlopen( request, context=context)
    # print(v)
    response = v.read()
    # print(response)
    data1 = json.loads( response )
    # print (data1)

    # Second API: Weather
    url2 = 'https://api.darksky.net/forecast/33cd834e9b0c38a7f1b9e9f00ed91679/37.8267,-122.4233'
    req = urllib.request.urlopen(url2, context=context)
    data2 = json.loads(req.read())
    # print (data2)

    # Third API: Chuck Norris
    url3 = "http://api.icndb.com/jokes/random"
    req = urllib.request.urlopen(url3, context=context)
    data3 = json.loads(req.read())
    print (data3)

    return render_template("template.html", holidays = data1['response']['holidays'][5], weather = data2['currently']['summary'], Chuckle = data3['value']['joke'])


if __name__ == "__main__":
    app.debug = True
    app.run()
