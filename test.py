import csv

file_1 = open('C:/Users/Slayer/Desktop/공유할것/collectl_output_Mix(원본) - 복사본.csv', 'r', encoding='utf-8')
read_1 = csv.reader(file_1)

# 20개
for line in read_1:

    print(line)

read_1 = csv.reader(file_1)

file_1.close()

