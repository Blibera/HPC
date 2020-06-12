import csv
import re

name = ["usr","sys","idl","wai","hiq","siq","read","writ","in","out","used","buff","cach","free","248","249","250","1m","5m","15m","recv","send","run","blk","new","read","writ","int","csw","majpf","minpf","alloc","free"]
print(len(name))
for l in range(1,2):

    node = str(l).zfill(2)
    new_name = []
    print(len(name))
    for i in range(len(name)):
        tol = "dstat" + node + "_" + name[i]
        new_name.append(tol)
    f = open("C:/Users/DI_Lab/Desktop/원본 데이터/Knl 멀티노드 (Flat)/knl02_dstat.csv", 'r', encoding='UTF8')
    ff = open("C:/Users/DI_Lab/Desktop/원본 데이터/Knl 멀티노드 (Flat)/1차 전처리/knl_dstat2.csv", "w",newline='', encoding='UTF8')
    write = csv.writer(ff)
    write.writerow(new_name)