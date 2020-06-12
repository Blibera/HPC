from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def item_collabor(movie_name):
    return item_based[movie_name].sort_values(ascending=False)[:6]

rating = pd.read_csv("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/Movielens/ratings.csv")
movie = pd.read_csv("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/Movielens/movies.csv")
rating = rating.drop('timestamp', axis=1)

movie = pd.merge(rating, movie, on="movieId")

movie_rating = movie.pivot_table('rating', index='title', columns='userId')
user_rating = movie.pivot_table('rating', index='userId', columns='title')

movie_rating_make = movie_rating.fillna(0)
user_rating_make = user_rating.fillna(0)

item_based = cosine_similarity(movie_rating_make)
print(movie_rating_make)
item_based = pd.DataFrame(data=item_based, index=movie_rating_make.index, columns= movie_rating_make.index)
print(item_based.head())

print(item_collabor("Godfather, The (1972)"))

