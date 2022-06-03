from flask import Flask, render_template
from toh import toh

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home of the Tower Of Hanoi solver!</h1>"

@app.route("/toh/<int:discCount>")
def toh_solved(discCount):
    print('Request for index page received')
    steps = []
    toh(steps,discCount,'A', 'C', 'B')
    return render_template('index.html',count=discCount, results = steps)