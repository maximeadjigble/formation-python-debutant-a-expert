from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/projets")
def projets():
    return render_template("projets.html")     

@app.route("/articles")
def articles():
    return render_template("articles.html")   

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