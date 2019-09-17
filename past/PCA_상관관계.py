import re

f = open("C:/Users/Slayer/Desktop/공유할것 (1)/data_x.txt", 'r')


def split(text):
    cleaned_text = re.sub('         ', ',', text)
    cleaned_text = re.sub('        ', ',', cleaned_text)
    cleaned_text = re.sub('       ', ',', cleaned_text)
    cleaned_text = re.sub('      ', ',', cleaned_text)
    cleaned_text = re.sub('     ', ',', cleaned_text)
    cleaned_text = re.sub('    ', ',', cleaned_text)
    cleaned_text = re.sub('   ', ',', cleaned_text)
    cleaned_text = re.sub('  ', ',', cleaned_text)
    cleaned_text = re.sub(' ', ',', cleaned_text)
    return cleaned_text

# 처음 한번만 싱행해서 Vn의 개수를 세서 정렬하기 위함
stack = 0

# Vn의 개수
count = 0
i = 0
v = []
while True:
    line = f.readline()
    if not line: break

    if stack ==0:
        stack = stack + 1
        line = split(line)
        count = line.count(',')
    else:
        line = split(line)
        j = str(i)
        j = "v" + j
        v = v.append(j)
        print(v)

    print(line)
    i = i + 1
print(v)
f.close()