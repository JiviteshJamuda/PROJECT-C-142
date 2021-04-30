import pandas as pd 
import csv

all_articles = []
with open('articles.csv', encoding ="utf8") as f:
    file = csv.reader(f)
    data = list(file)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []

# article = all_articles[0]
# # all_movies = all_movies[1:]
# liked_articles.append(article)
# all_articles.pop(0)
# print(liked_articles[0][4])