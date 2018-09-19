# Alexander Liu
# SoftDev1 pd7
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask
app = Flask(__name__)


#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

@app.route('/home')
def homepage():
    return '''<h1 style="text-align:center"> Welcome <h1>
    <h2><a id="top">There is a link at the bottom of the page!</a></h2>
    <b> Star Wars summary <b>
    <p> The Chancellor has been captured by a revolt leader General Grievous, but Obi-Wan </br>
    and Anakin rescue him heroically. The Chancellor, seeking to draw out Anakin's dark </br>
    side, demands that Anakin assassinate Dooku, which he does. Anakin is </br>
    dealing with his demons, including visions of Padme dying in childbirth. The Council </br>
    declines to elevate him to Master status, so the Chancellor puts him on the Jedi Council </br>
    as his representative (spy). He also brags to Anakin that he knows how to harness the dark </br>
    side to cheat death — though you can't learn that from any (dismissively) Jedi. But (wait for it!), </br>
    it's a trap. Anakin eventually figures out that the Chancellor is a Sith Lord, but when the Jedi </br>
    try to arrest him, Anakin comes to his aid because he still wants to save Padme from the visions </br>
    of death. The Chancellor makes Anakin his apprentice and dubs him Darth Vader. He also orders him </br>
    to kill everyone, including younglings, though a few Jedi, including Yoda, escape. Obi-Wan tries </br>
    to stop him with an epic lightsaber battle on the molten planet Mustafar, leaving Anakin next to </br>
    a lava river as little more than a burnt up torso. The Chancellor saves him, puts him in Darth </br>
    Vader's famous black suit and they start the Death Star. Padme dies in childbirth and her twins, </br>
    Luke and Leia are separated and hidden from the now-Empire, with Leia going to Alderaan and Luke </br>
    ending up on Tatooine, with Obi-Wan going into exile there to watch over the boy. <p>


    <a href="https://media.giphy.com/media/l1Ksy7xHM9qhumWxa/giphy.gif"> When you relearn html :(</a>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <button onclick="myFunction()">Go to top</button>
    <script>
    function myFunction() {
    location.href = "#top";
    }
    </script>
    <button onclick="location.href='/secrets'">sites</button>
    '''
@app.route('/second')
def drinks():
    return 'the second route'

@app.route('/secrets')
def food():
    return '''a list:
    <ul>
    <li><a href="http://www.nooooooooooooooo.com/"> one </a></li>
    <li><a href="https://www.pointerpointer.com/"> two </a></li>
    <li><a href="https://www.snapbubbles.com"> three </a></li>
    <li><a href="https://www.sanger.dk"> four </a></li>
    <li><a href="https://www.zoomquilt.org"> five </a></li>
    </ul>
    <button onclick="location.href='/home'">home</button>
    '''



if __name__ == '__main__':
    app.debug = True
    app.run()
