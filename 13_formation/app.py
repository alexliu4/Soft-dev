from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def template_tester():
    return render_template("input.html")

@app.route("/auth", methods = ["POST", "GET"])
def authenticate():
    print(app)
    print(request)

    dictionary = {}

    if request.method=="GET":
        dictionary = request.args

    if request.method=="POST":
        dictionary = request.form

    print(app)
    print(request)
    print(request.method)
    return render_template("result.html",
                            foo = "hey",
                            field1 = "username" ,
                            key1 = dictionary['username'] ,
                            field2 = "method",
                            key2 = (request.method))
    #return '<b>Greetings</b> <br> <br>' + 'method type:' + (request.method) + '<br>username: ' + request.args['username'] + '<b><br>See you next time!</br>'

if __name__ == "__main__":
    app.debug = True
    app.run()
