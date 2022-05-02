import os
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db_articles import liste_articles
from db_projets import liste_projets

N_PROJETS = 3
N_ARTICLES = 2
DOSSIER_UPLOAD = "static/images/"

app = Flask(__name__)

#Base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# flask db init
# flask db migrate -m "Commentaire"
# flask db upgrade

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150))
    slug = db.Column(db.String(150))
    contenu = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article[{self.id}] {self.titre}>"

#URLS
@app.route("/")
def accueil():
    return render_template("index.html", projets=liste_projets[:N_PROJETS], articles=liste_articles[:N_ARTICLES])

@app.route("/projets/creer", methods=["GET", "POST"])
def creer_projet():
    if request.method == 'POST':
        titre = request.form['titre']
        slug = request.form['slug']
        description = request.form['description']
        fichier = request.files['fichier']
        # print(titre, slug, description, fichier.filename)

        image_url = '/static/images/thumb_small.png'
        if fichier.filename != '':
            image_url = f'/static/images/{fichier.filename}'
            fichier.save(os.path.join(DOSSIER_UPLOAD, fichier.filename))

        #Vérifier que l'utilisateur est connecté
        liste_projets.append({
                "titre": titre,
                "slug": slug,
                "description": description,
                "image_url": image_url
            }) 
        return redirect(url_for('projets'))
    return render_template("creer_projet.html") 

@app.route("/projets/")
@app.route("/projets/<string:slug>")
def projets(slug=""):
    if slug: 
        for projet in liste_projets:
            if projet['slug'] == slug:
                return render_template('projet.html', projet=projet)
    return render_template("projets.html", projets=liste_projets)     

@app.route("/articles/creer", methods=["GET", "POST"])
def creer_article():
    if request.method == 'POST':
        titre = request.form['titre']
        slug = request.form['slug']
        contenu = request.form['contenu']
        print(titre, slug, contenu)
        #Vérifier que l'utilisateur est connecté
        liste_articles.append({
                "titre": titre,
                "slug": slug,
                "contenu": contenu
            }) 
        return redirect(url_for('articles'))
    return render_template("creer_article.html")   

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