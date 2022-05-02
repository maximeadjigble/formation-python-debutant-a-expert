from flask import Flask, render_template
from db_articles import liste_articles
from db_projets import liste_projets

N_PROJETS = 3
N_ARTICLES = 2

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html", projets=liste_projets[:N_PROJETS], articles=liste_articles[:N_ARTICLES])

@app.route("/projets")
def projets():
    return render_template("projets.html", projets=liste_projets)     

@app.route("/articles")
def articles():
    return render_template("articles.html", articles=liste_articles)   

@app.route("/login")
def login():
    return render_template("login.html")   

@app.errorhandler(404)
def page_404(error):
    # print(error)
    return render_template('404.html'), 404

@app.route("/jinja")
def jinja():
    return render_template("jinja.html", prenom="Antoine", afficher=False, utilisateurs=['Alex','Romaric', 'Martin'])