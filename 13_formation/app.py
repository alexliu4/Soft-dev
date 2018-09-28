from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def template_tester():
    return render_template("input.html"
    )

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args['username'])
    print(request.method)
    return '<b>Greetings</b> <br> <br>' + 'method type:' + (request.method) + '<br>username: ' + request.args['username'] + '<b><br>See you next time!</br>'

if __name__ == "__main__":
    app.debug = True
    app.run()
