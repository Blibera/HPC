import pandas as pd

for l in range(1,18):
    if l == 6:
        pass
    else:
        data = pd.read_csv('C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/' + str(l) + '.csv')
        #data = pd.read_csv('C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/21개 원본 파일.csv')
        print(data.head(10))

        df = pd.DataFrame(data)
        corr = df.corr(method='pearson')
        print(corr)

        corr.to_csv('C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/' + str(l) + '(피어슨).csv')
        #corr.to_csv('C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/21개 원본 파일.csv')