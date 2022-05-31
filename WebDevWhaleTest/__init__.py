from flask  import Flask, redirect, url_for
from flask.templating import render_template
from flask import request


app = Flask(__name__)
#@app.route("/name")


@app.route("/home")
def home():
    
    return render_template("index.html")

@app.route("/home/spermwhale")
def SpermWhale():
    
    return render_template("spermwhale.html", title='SpermWhale')

@app.route("/home/bluemwhale")
def BlueWhale():
    
    return render_template("bluewhale.html", title='BlueWhale')

@app.route("/home/seiwhale")
def SeiWhale():
    
    return render_template("seiwhale.html", title='SeiWhale')


if __name__ == "__main__":
    app.debug = True
    app.run()
   