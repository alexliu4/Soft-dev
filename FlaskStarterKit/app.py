# Karen Li
# SoftDev1 pd7
# 
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def home():  
    return render_template('template.html')

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return ""

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
