import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from sklearn.preprocessing import RobustScaler

name = "epyc_single_perf"

df = pd.read_csv("C:/Users/DI_Lab/Desktop/클러스터/" + str(name) + ".csv")

x = df.values.astype(float)
"""
robust_scaler = RobustScaler()
robust_scaler.fit(x)
X_robust_scaled = robust_scaler.transform(x)
a = pd.DataFrame(X_robust_scaled)
print(a)
"""
min_max = preprocessing.MinMaxScaler()

x_scale = min_max.fit_transform(x)

df = pd.DataFrame(x_scale, columns=df.columns)



df.to_csv("C:/Users/DI_Lab/Desktop/클러스터/" + str(name) + "_정규화.csv")

