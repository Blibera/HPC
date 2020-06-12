from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.model_selection import train_test_split

def item_collabor(movie_name):
    return item_based[movie_name].sort_values(ascending=False)[:6]

Full_data = pd.read_csv("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/pd test.csv", encoding="euc-kr")
item_movie_rating = Full_data.pivot_table('rate', index = 'nickname', columns='movie_name').fillna(0)
item_movie_rating["count"] = item_movie_rating.sum(axis=1)

print(item_movie_rating)
print("★★★★★★★★★★★★★★★★★★")
print("★★★★★★★★★★★★★★★★★★")
test_set = item_movie_rating[(item_movie_rating["count"] >= 100)]
test_set = test_set.drop('count', axis=1)
print(test_set)
test_set = test_set.T
item_based = cosine_similarity(test_set)
item_based = pd.DataFrame(data=item_based, index=test_set.index, columns= test_set.index)
print(item_based.head())

print(item_collabor("데드풀 2"))


