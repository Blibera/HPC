from sklearn.preprocessing import StandardScaler

a = [[1],[2],[3],[1],[2],[5],[12],[5],[2],[215],[2151],[521],[521521],[51]]

aa = [[10], [9], [8], [6], [2]]
scaler = StandardScaler()
a = scaler.fit_transform(a)
print(a)
print(a.mean())
print(a.std())
