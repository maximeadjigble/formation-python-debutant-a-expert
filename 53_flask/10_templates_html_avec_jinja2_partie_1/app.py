from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/jinja")
def jinja():
    return render_template("jinja.html")