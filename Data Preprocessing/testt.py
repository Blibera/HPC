import csv
import re

f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/3차 전처리/활용 데이터/dstat.csv", 'r', encoding='UTF8')
n = "﻿Application,total cpu usage:usr,total cpu usage:sys,total cpu usage:idl,total cpu usage:wai,total cpu usage:stl,read,writ,recv,send,in,out,int,csw,run,blk,new,used,free,buff,cach,used,free,1m,5m,15m,read,writ"
a = re.sub(',','\",\"',n)
print(a)

