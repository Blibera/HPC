from sklearn.model_selection import GridSearchCV
import sklearn.svm as svm
import sklearn.metrics as mt
from sklearn.model_selection import cross_val_score, cross_validate
import sklearn.datasets as d
import pandas as pd
from sklearn.model_selection import train_test_split
import time
start = time.time()  # 시작 시간 저장
df = pd.read_csv("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/6. HMM 사용 데이터/svm/1초/5개/1 (t) - 변화율 t - 5 - power.csv")
X = df.drop("total", axis=1)
y = df["total"]

svm_clf = svm.SVC(kernel = 'rbf',random_state=100)
#parameters = {'C': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
#             'gamma':[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]}
parameters = {'C': [2500],
              'gamma':[0.5]}
grid_svm = GridSearchCV(svm_clf,
                      param_grid = parameters, cv = 2)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                      test_size = 0.2, random_state = 100)
grid_svm.fit(X_train, y_train)

result = pd.DataFrame(grid_svm.cv_results_['params'])
result['mean_test_score'] = grid_svm.cv_results_['mean_test_score']
print(result.sort_values(by='mean_test_score', ascending=False))

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
