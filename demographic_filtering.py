import pandas as pd
import numpy as np 

df = pd.read_csv('articles.csv')

q_articles = df.sort_values('total_events', ascending=False)
output = q_articles.head(20).values.tolist()
# print(output)