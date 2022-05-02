from flask import Flask, render_template, request
from markupsafe import escape
from db_articles import liste_articles
from db_projets import liste_projets

N_PROJETS = 3
N_ARTICLES = 2

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html", projets=liste_projets[:N_PROJETS], articles=liste_articles[:N_ARTICLES])

@app.route("/projets/")
@app.route("/projets/<string:slug>")
def projets(slug=""):
    if slug: 
        for projet in liste_projets:
            if projet['slug'] == slug:
                return render_template('projet.html', projet=projet)
    return render_template("projets.html", projets=liste_projets)     

@app.route("/articles/")
@app.route("/articles/<string:slug>")
def articles(slug=""):
    if slug:
       for article in liste_articles:
            if article['slug'] == slug:
                return render_template('article.html', article=article)        
    return render_template("articles.html", articles=liste_articles)   

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # print(username, password)
        return "<h1>Utilisateur Connecté</h1>"
    return render_template("login.html")   

@app.errorhandler(404)
def page_404(error):
    # print(error)
    return render_template('404.html'), 404

@app.route("/jinja")
def jinja():
    return render_template("jinja.html", prenom="Antoine", afficher=False, utilisateurs=['Alex','Romaric', 'Martin'])