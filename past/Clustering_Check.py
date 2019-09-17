import csv
import re


a = "C:/Users/Slayer/Desktop/Kisti/작업폴더/result_cluster.csv"
f = open(a, 'r', encoding='UTF-8')
i = 0
one = 0
six = 0
eleven = 0
two = 0
seven = 0
twelve = 0
three = 0
eight = 0
thirteen = 0
four = 0
nine = 0
five = 0
ten = 0


while True:
    line = f.readline()
    if not line: break

    if i < 207:
        if line == 1:
            one = one + 1
        elif line == 2:
            two = two + 1
        elif line == 3:
            three = three + 1
        elif line == 4:
            four = four + 1
        elif line == 5:
            five = five + 1
        elif line == 6:
            six = six + 1
        elif line == 7:
            seven = seven + 1
        elif line == 8:
            eight = eight + 1
        elif line == 9:
            nine = nine + 1
        elif line == 10:
            ten = ten + 1
        elif line == 11:
            eleven = eleven + 1
        elif line == 12:
            twelve = twelve + 1
        elif line == 13:
            thirteen = thirteen + 1

    elif 207 <= i and i < 389:
        if i == 207:
            print(one, six, )
            one = 0
            six = 0
            eleven = 0
            two = 0
            seven = 0
            twelve = 0
            three = 0
            eight = 0
            thirteen = 0
            four = 0
            nine = 0
            five = 0
            ten = 0

        if line == 1:
            one = one + 1
        elif line == 2:
            two = two + 1
        elif line == 3:
            three = three + 1
        elif line == 4:
            four = four + 1
        elif line == 5:
            five = five + 1
        elif line == 6:
            six = six + 1
        elif line == 7:
            seven = seven + 1
        elif line == 8:
            eight = eight + 1
        elif line == 9:
            nine = nine + 1
        elif line == 10:
            ten = ten + 1
        elif line == 11:
            eleven = eleven + 1
        elif line == 12:
            twelve = twelve + 1
        elif line == 13:
            thirteen = thirteen + 1
    elif 389 <= i and i < 540:
        print(i)
    elif 540 <= i and i < 754:
        print("=======================================================")
    elif 754 <= i and i < 894:
        print(i)
    elif 894 <= i and i < 1068:
        print("=======================================================")
    elif 1068 <= i and i < 1593:
        print(i)
    else:
        print("=======================================================")
    i = i + 1