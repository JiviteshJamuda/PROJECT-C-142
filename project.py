from flask import Flask, jsonify, request
import csv
import pandas as pd
from demographic_filtering import output
from content_filtering import get_recommendation, cosine_sim
from storage import all_articles, liked_articles, not_liked_articles

app = Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        'data'   : all_articles[0],
        'status' : 'success'
    }),200

@app.route('/liked-article', methods = ['POST'])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status' : 'success',
    }),200

@app.route('/not-liked-article', methods = ['POST'])
def not_liked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status' : 'success',
    }),200

@app.route('/popular-article')

def popular_article():
    article_data = []
    for article in output:
        d = {
            # 'id'        : article[0],
            # 'index'     : article[1],
            # 'timestamp' : article[2],
            # 'content_id': article[4],
            # 'url'       : article[11],
            'title'     : article[12],
            # 'text'      : article[13],
            # 'lang'      : article[14],
        }
        article_data.append(d)
    return jsonify({
        'data' : article_data,
        'status' : 'success'
    }),200

@app.route('/recommended-article')

def recommended_article():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendation(int(liked_articles[0][4]), cosine_sim)

        for data in output:
            all_recommended.append(data)
    
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))

    article_data = []
    for data in all_recommended:
        d = { 'data' : all_recommended[0] }
        article_data.append(d)
   
    return jsonify({
        'data'   : article_data,
        'status' : 'success'
    }),200

if __name__ == '__main__':
    app.run()