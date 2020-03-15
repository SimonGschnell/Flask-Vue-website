from . import app, db
from flask import request, render_template, jsonify
import requests
from random import *
from .models import Projects


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.route('/api/random')
def random_number():
    response={
        'randomNumber':randint(1,100)
    }
    return jsonify(response)

@app.route('/api/projects')
def projects():
    response = []
    for i in Projects.query.all():
        item ={ "title":i.title, "description":i.description, "logo":i.logo, "date":i.date}
        response.append(item)

    return jsonify(response)


@app.route('/api/navbar/items')
def nav_items():
    pass