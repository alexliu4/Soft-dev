# Alex Liu
# SoftDev1 pd7
# K26 -- A RESTful Journey Skyward
# 2018-11-15

from flask import Flask, render_template
import urllib.request
import json
import ssl
app = Flask(__name__)

print("============================================================")
apikey = "30370a68e63546a520f00a0640a999ac0e911cad"
url1 = "https://www.calendarindex.com/api/v1/holidays?country=US&year=2018&state=NY&api_key=" #url for new york
context = ssl._create_unverified_context()
print("=============" + url1 + "=============\n\n")
user_agent = "Mozilla"
headers = {'User-Agent': user_agent, }

@app.route('/')
def home():
    request = urllib.request.Request(url1 + apikey, None, headers)
    v = urllib.request.urlopen( request, context=context)
    print(v)

    response = v.read()
    print(response)

    data = json.loads( response )
    print (data)

    return render_template("template.html", holidays = data)


if __name__ == "__main__":
    app.debug = True
    app.run()
