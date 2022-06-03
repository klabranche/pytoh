from flask import Flask, render_template
from toh import toh

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/toh/<int:discCount>")
def toh_solved(discCount):
    print('Request for index page received')
    steps = []
    toh(discCount,'A', 'C', 'B')
    return render_template('index.html',count=discCount, results = steps)