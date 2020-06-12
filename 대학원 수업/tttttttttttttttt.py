from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

def recommend_movies (df_svd_preds, user_id, ori_movies_df, ori_ratings_df, num_recommandations=5):
    jjj = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본 - FULL.csv', encoding='utf-8-sig')
    item_based = jjj.pivot_table('rate', index='nickname', columns='movie_name')
    item_based.insert(0, 'New_ID', range(0, 0 + len(item_based)))
    kk = item_based["New_ID"]
    print(kk)
    user_id_num = kk.loc["yunm****"]
    sorted_user_predictions = df_svd_preds.iloc[user_id_num].sort_values(ascending=False)
    user_data = ori_ratings_df[ori_ratings_df.nickname == user_id]
    print(sorted_user_predictions)
    print("★★★★★★★★★★★★★★")
    print("★★★★★★★★★★★★★★")
    print(user_data)
    print("===================")
    print("===================")
    print(ori_movies_df)
    user_history = user_data.merge(ori_movies_df, on='movie_name').sort_values(['rate'], ascending=False)
    print(user_history)
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    recommendations = ori_movies_df[~ori_movies_df['movie_name'].isin(user_history['movie_name'])]
    recommendations = recommendations.merge(pd.DataFrame(sorted_user_predictions).reset_index(), on='movie_name')
    recommendations = recommendations.drop_duplicates('movie_name',keep='first')
    print(recommendations)
    print("★★★★★★★★★★★★★★")
    print("★★★★★★★★★★★★★★")
    recommendations = recommendations.rename(columns = {user_id_num: 'Predictions'}).sort_values('Predictions', ascending = False).iloc[:num_recommandations, :]

    return ori_movies_df, recommendations
Full_data = pd.read_csv("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본 - FULL.csv", encoding='utf-8-sig')
movie_data = Full_data[['movie_name','nickname']]
rating_data = Full_data[['rate','nickname','movie_name']]
train_set, Full_data = train_test_split(Full_data, test_size = 0.3)
print(movie_data)
print(rating_data)
item_movie_rating_Full = Full_data.pivot_table(values='rate', index = 'nickname', columns='movie_name').fillna(0)

item_movie_rating = np.asarray(item_movie_rating_Full)
user_rating_mean = np.mean(item_movie_rating, axis=1)
matrix_user_mean = item_movie_rating - user_rating_mean.reshape(-1,1)

U, sigma, Vt = svds(matrix_user_mean, k=12)
sigma = np.diag(sigma)
svd_user_rating = np.dot(np.dot(U, sigma), Vt) + user_rating_mean.reshape(-1,1)
df_svd_preds = pd.DataFrame(svd_user_rating, columns=item_movie_rating_Full.columns)
print("★★★★★★★★★★★★★★★★★★★★★★★★★")
print("★★★★★★★★★★★★★★★★★★★★★★★★★")
print("★★★★★★★★★★★★★★★★★★★★★★★★★")
print(df_svd_preds.head(10))
already_rated, predictions = recommend_movies(df_svd_preds, "tomb****", movie_data, rating_data, 10)
print(already_rated)
predictions.to_csv("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/moviessssssssssss.csv", mode='w', encoding="euc-kr")
print(predictions.head(10))