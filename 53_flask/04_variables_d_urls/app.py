from flask import Flask
from markupsafe import escape
 
app = Flask(__name__)

@app.route("/")
def accueil():
    return "Hello World!"

@app.route("/projets")
def projets():
    return ''' 
    <h2>Mes projets</h2>
    <ul> 
        <li><a href="/projet/premier-projet">Projet 1</a></li>
        <li><a href="/projet/deuxieme-projet">Projet 2</a></li>
        <li><a href="/projet/troisieme-projet">Projet 3</a></li>
    </ul>
    '''

@app.route("/projet/<int:slug>")
def projet(slug):
    # slug = escape(slug)
    return str(slug)
