import sklearn.datasets as d
import sklearn.svm as svm
import sklearn.metrics as mt
from sklearn.model_selection import cross_val_score, cross_validate
import pandas as pd
# breast_cancer 데이터 셋 로드
name = ""
df = pd.read_csv("C:/Users/DI_lab/Desktop/SVM 작업폴더/이미지 사용 파일/" + str(name) + ".csv")


svm_clf =svm.SVC(kernel = 'linear')

# 교차검증
X = df.iloc[:,:-5]
print(X)
y = df['CPU']
print(y)

scores = cross_val_score(svm_clf, X, y, cv = 2)
scores
print('교차검증 평균: ', scores.mean())
pd.DataFrame(cross_validate(svm_clf, X, y, cv =2))

print('교차검증 평균: ', scores.mean())