from flask import Flask, jsonify, request
import csv
import pandas as pd

app = Flask(__name__)

all_articles = []
with open('articles.csv', encoding ="utf8") as f:
    file = csv.reader(f)
    data = list(file)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []

@app.route('/get-article')
def get_article():
    return jsonify({
        'data'   : all_articles[0],
        'status' : 'success'
    }),200

@app.route('/liked-article', methods = ['POST'])
def liked_article():
    article = all_articles[0]
    # all_movies = all_movies[1:]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status' : 'success',
    }),201

@app.route('/not-liked-article', methods = ['POST'])
def not_liked_article():
    article = all_articles[0]
    # all_movies = all_movies[1:]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status' : 'success',
    }),202

if __name__ == '__main__':
    app.run()