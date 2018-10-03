from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_tester():
    return render_template("thing.html",
                             foo = "oof",
                             collection = [0,1,1,2,3,5,8]
                               )


if __name__ == "__main__":
    app.debug = True
    app.run()
