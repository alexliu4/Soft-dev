# Maggie Zhao & Jiajie Mai & Alexander Liu
# SoftDev1 pd7
# K14-- Do I Know You?
# 2018-10-02



from flask import Flask, render_template, request, session, url_for, redirect, flash
import os
app = Flask(__name__)

username = 'alex'
password = 'starwars4'

@app.route('/')
def disp_login():
    loginMess = "Please enter a valid username and password."
    flash(loginMess)
    return render_template("foot.html")

#what is the difference between render_template, redirect, and url_for?
@app.route('/auth', methods = ['POST'] )
def authenticate():

    session['username'] = request.form['username']
    session['password'] = request.form['password']
    #print(session)

    ### Invalid username: ===================================
    if session['username'] != username:
        errorMess = "*cue sad trombone music* \n It looks like you've entered an invalid username. Please try again."
        #print('bad username')
        flash(errorMess)
        return (render_template("foot.html", message = errorMess))

    ### Invalid password: ===================================
    elif session['password'] != password:
        errorMess = "*cue sad trombone music* \n It looks like your password does not match your username. Please try again."
        print('bad password')
        flash(errorMess)
        return  (render_template("foot.html", message = errorMess))

    ### Both username and password are valid ================
    elif (session['username'] == username and session['password'] == password):
        return render_template("welcome.html")

    ### All other invalid cases =============================
    else:
        errorMess = "Oops! Looks like something went wrong. Please try again."
        flash(errorMess)
        return ( (render_template("foot.html", message = errorMess )))
#
#     #print (url_for('disp_login'))
#     #print (url_for('authenticate'))
#     #return redirect(url_for("disp_login"))
app.secret_key = os.urandom(32)

@app.route('/logout')
def logout():
    return ( render_template ( "foot.html", message = "You have been successfully logged out."))

    print(app)
    print(request) ##prints returned URL with auth tags
    print(request.args) ## gives immutabledict based on names of input fields (ie username & sub1)
    print(request.args['username'])
    print(request.headers)
    return "Waaaa hooo HAAAH"

if __name__ == "__main__":
    app.debug = True
    app.run()
