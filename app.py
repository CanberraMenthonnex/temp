from flask import Flask
from markupsafe import escape
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/article/<int:id>')
def article(id):
    file_path = f'IA/datasets/data-{id}.txt'
    data = pd.read_csv(file_path, sep='\t', engine='python')
    return data.to_html()


@app.route('/api')
def get_api():
    return {
        "username": "Lucas",
        "theme": "Un espion dans la ville",
        "image": "Une url",
    }

@app.route('/<prompt>')
def about(prompt):
    return prompt