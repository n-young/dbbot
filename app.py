from flask import Flask, flash, redirect, render_template, request, session, abort, current_app
from generate import generateOne

app = Flask(__name__)

@app.route("/")
def homeRoute():
    return render_template('index.html', result="Generate a Dear Blueno post! Add a prefix if you'd like, and let the mAcHinE lEaRnInG do the rest! Results will be shown here.")

@app.route("/generate")
def generateRoute():
    return render_template('index.html', result=generateOne(request.args.get('prefix')))

if __name__ == "__main__":
    app.run()