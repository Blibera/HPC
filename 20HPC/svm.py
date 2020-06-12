import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from warnings import simplefilter
import time



# 작업 코드


simplefilter(action='ignore', category=FutureWarning)

def svm(i):
    X = df.drop("rate", axis=1)
    y = df["rate"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)
    svclassifier = SVC(kernel='rbf', degree=i)
    svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return acc

start = time.time()  # 시작 시간 저장
df = pd.read_csv("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/6. HMM 사용 데이터/svm/test - svm 3 - 9.csv")


i = 0
max_list = []
num_list = []
for j in range(0,1):
    max = 0
    acc = 0
    for i in range(3,4):
        if i == 3:
            max = svm(i)
            acc_num = i
        acc = svm(i)
        if max < acc:
            max = acc
            acc_num = i
    max_list.append(max)
    num_list.append(acc_num)
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(max_list)
print(num_list)
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
