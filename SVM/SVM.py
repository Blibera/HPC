import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from warnings import simplefilter
import time
import time



# 작업 코드


simplefilter(action='ignore', category=FutureWarning)
name_list = ["1", "3", "5", "10"]

def svm(i):
    X = df.drop(name, axis=1)
    y = df[name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    svclassifier = SVC(kernel='rbf', degree=i)
    svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return acc

for k in range(0,4):
    start = time.time()  # 시작 시간 저장
    df = pd.read_csv("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/knl_Data/막 다루는 곳/Up_down(" + str(name_list[k]) +  "% 버전).csv")

    name = "Perf_node01_power_energy_pkg_"



    i = 0
    max_list = []
    num_list = []
    for j in range(0,3):
        max = 0
        acc = 0
        for i in range(3,14):
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
    print(name_list[k])
    print(max_list)
    print(num_list)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
