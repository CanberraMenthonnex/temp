from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/<prompt>')
def about(prompt):
    return 'The page for ' + escape(prompt)