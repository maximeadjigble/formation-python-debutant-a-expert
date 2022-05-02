from flask import Flask
 
app = Flask(__name__)

@app.route("/")
def accueil():
    return "Hello World!"

@app.route("/projets")
def projets():
    return "Page de projets"

@app.route("/articles")
def articles():
    return "Page d'articles"

@app.route("/login")
def login():
    return "Page de Login"