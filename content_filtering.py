import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from storage import all_articles, liked_articles

df = pd.read_csv('articles.csv')
df = df[df['title'].notna()]

count = CountVectorizer(stop_words = 'english')
count_matrix = count.fit_transform(df['title'])
# print(count_matrix)

cosine_sim = cosine_similarity(count_matrix, count_matrix)
df = df.reset_index()
indices = pd.Series(df.index, index = df['contentId'])

def get_recommendation(title, cosine_sim):
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key = lambda x : x[1], reverse=True)
  sim_scores = sim_scores[1:11]
  article_indices = [i [0] for i in sim_scores]
  return df['title'].iloc[article_indices]

# get_recommendation(-4029704725707465084, cosine_sim)

# article = all_articles[0]
# # all_movies = all_movies[1:]
# liked_articles.append(article)
# all_articles.pop(0)
# # print(liked_articles[0][4])
# output = get_recommendation(int(liked_articles[0][4]), cosine_sim)
# print(output)