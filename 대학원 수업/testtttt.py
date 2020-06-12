from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings

orri = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본 - FULL.csv', encoding='utf-8-sig')
df_ratings = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본 - FULL.csv', encoding='utf-8-sig')
df_movies = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본 - FULL.csv', encoding='utf-8-sig')
original_data = orri[orri.columns.difference(['Unnamed: 0'])]
original_data = original_data[original_data.columns.difference(['Unnamed: 0.1'])]

# tpye을 따로 저장하여 데이터를 분할
type = original_data['type']
original_data = original_data[original_data.columns.difference(['type'])]
original_data.loc[:,['movie_name']] = original_data.loc[:,['movie_name']].astype('category')
original_data.loc[:,['nickname']] = original_data.loc[:,['nickname']].astype('category')
original_data.loc[:,['rate']] = original_data.loc[:,['rate']].astype('float32')

# item_based를 위한 pivot table 생성
item_based = original_data.pivot_table('rate', index = 'nickname', columns='movie_name')

print("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
# 결측값 0으로 넣기
item_based = item_based.fillna(0)

# matrix는 pivot_table 값을 numpy matrix로 만든 것
matrix = item_based.values

# user_ratings_mean은 사용자의 평균 평점
user_ratings_mean = np.mean(matrix, axis = 1)

# R_user_mean : 사용자-영화에 대해 사용자 평균 평점을 뺀 것.
matrix_user_mean = matrix - user_ratings_mean.reshape(-1, 1)

U, sigma, Vt = svds(matrix_user_mean, k = 12)
print(U.shape)
print(sigma.shape)
print(Vt.shape)

sigma = np.diag(sigma)
svd_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns = item_based.columns)

print(df_svd_preds)
print("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
print("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
print("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
jjj = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본 - FULL.csv', encoding='utf-8-sig')
item_based = jjj.pivot_table('rate', index = 'nickname', columns='movie_name')
item_based.insert(0, 'New_ID', range(0, 0 + len(item_based)))
kk = item_based["New_ID"]
kk = kk.loc["zzxx****"]
print(kk)

def recommend_movies(df_svd_preds, user_id, user_num, ori_movies_df, ori_ratings_df, num_recommendations=5):
    user_row_number = user_num - 1

    # 최종적으로 만든 pred_df에서 사용자 index에 따라 영화 데이터 정렬 -> 영화 평점이 높은 순으로 정렬 됌
    sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False)

    # 원본 평점 데이터에서 user id에 해당하는 데이터를 뽑아낸다.
    user_data = ori_ratings_df[ori_ratings_df.nickname == user_id]
    print(user_data)
    # 위에서 뽑은 user_data와 원본 영화 데이터를 합친다.
    user_history = user_data.merge(ori_movies_df, on='movie_name').sort_values(['rate'], ascending=False)

    # 원본 영화 데이터에서 사용자가 본 영화 데이터를 제외한 데이터를 추출
    recommendations = ori_movies_df[~ori_movies_df['movie_name'].isin(user_history['movie_name'])]
    # 사용자의 영화 평점이 높은 순으로 정렬된 데이터와 위 recommendations을 합친다.
    recommendations = recommendations.merge(pd.DataFrame(sorted_user_predictions).reset_index(), on='movie_name')
    # 컬럼 이름 바꾸고 정렬해서 return
    recommendations = recommendations.rename(columns={user_row_number: 'Predictions'}).sort_values('Predictions',
                                                                                                   ascending=False).iloc[
                      :num_recommendations, :]

    return user_history, recommendations

already_rated, predictions = recommend_movies(df_svd_preds, "zzxx****", kk, df_movies, df_ratings, 10)

print(matrix)





