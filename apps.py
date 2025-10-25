import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

os.system('unzip flask-app.zip;python run.py &')

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")

