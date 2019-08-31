from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")

def hello():
    return render_template("/home/lista.html")

app.run()