# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h_K1kt6CUW1_k7SR9Ailm770-DRuSqtd
"""



"""# **Movie Recomendation System**
**Recommendar System** is a system that seeks to predict or filter prefrences according to the users choices. Recommendar system are utilized in veriety of area including movies,music, news, books,resaerch articles, etc.. ,and product in genral.Recommendar system produce a list of recommendations in any of the two ways-

**Collaborative filterings** filtering approaches builds a model from the past behaviour that user may have interest in.

**Content-based filtering** content-based filtering approaches uses a series of discrete characteristics of an item in order to recommend additional items with similar properties. content-based filtering methods are totally based on a description of the item and a profile of the users prefrences. it recomends items based on the user past prefrences. lets develop a basic recommendation system using python and pandas.

# **Import Library**
"""

import pandas as pd

import numpy as np

"""# **Import Datasets**"""

df = pd .read_csv(r'https://raw.githubusercontent.com/YBIFoundation/Dataset/refs/heads/main/Movies%20Recommendation.csv')

df.head()

df.info()

df.shape

df.columns

"""# **Get Feature Selection**"""

df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

df_features.shape

df_features

x = df_features['Movie_Genre'] + '' + df_features['Movie_Keywords'] + '' + df_features['Movie_Tagline'] + '' + df_features['Movie_Cast'] + '' + df_features['Movie_Director']

x

x.shape

"""# **Get Feature Text Conversion to Token**"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

"""# **Get Similarity Score using Cosine Similarity**

cosine_similarity computers the L2-normalized dot product of vectors. Euclidean(L2) normalization projects the vectors onto the unit sphere,and their dot product is then the cosine of the angle between the points denoted by the vectors.
"""

from sklearn.metrics.pairwise import cosine_similarity

similarity_Score = cosine_similarity(x)

similarity_Score

similarity_Score.shape

"""# **Get Movie Name as Input from User and Validate for Closest Spelling**"""

Favourite_Movie_Name = input('Enter your favourite movie name :')

All_Movie_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name,All_Movie_Title_List)
print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]
  print(Close_Match)

Index_of_close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_close_Match_Movie)

# getting a list of similar movie

Recommendation_Score = list(enumerate(similarity_Score[Index_of_close_Match_Movie]))
print(Recommendation_Score)

len(Recommendation_Score)

"""# **Get All Movie Sort Based on Recommendation Score wrt Favourite Movie**"""

# sorting the movie based on their similarity score
sorted_similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
print(sorted_similar_Movies)

# print the name of similar movies based on the index
print('Top 30 Movies Suggested for You:\n')
i = 1
for movie in sorted_similar_Movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if(i<31):
    print(i, '.',title_from_index)
    i+=1

"""# **Top 10 Movie Recommendation System**"""

Movie_Name = input('Enter your favourite movie name : ')
list_of_all_titles = df['Movie_Title'].tolist()

Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)

Close_Match = Find_Close_Match[0]

Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]

Recommendation_Score = list(enumerate(similarity_Score[Index_of_Movie]))

sorted_similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)

print('Top 10 Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:

  index = movie[0]
  title_from_index = df[df.Movie_ID==index]['Movie_Title'].values
  if (i<11):
    print(i, '.',title_from_index)
    i+=1