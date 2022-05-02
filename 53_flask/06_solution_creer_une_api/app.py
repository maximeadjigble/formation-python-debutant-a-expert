from flask import Flask
from donnees import donnees
from markupsafe import escape
 
app = Flask(__name__)

@app.route("/")
def accueil():
    return "Hello World!"

@app.route("/celebrites")
def celebrites():
    template = ""
    for slug, donne in donnees.items():
        template += f'<li><a href="/api/{slug}">{slug}</a></li>'
    return f"<h2>Célébrités</h2><ul>{template}</ul>"

@app.route("/api/<string:slug>")
def celebrite(slug):
    slug = escape(slug)
    return donnees[slug] if slug in donnees else {"erreur": "Non existant"}
