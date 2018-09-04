import re
import csv

f = open("C:/Users/Slayer/Desktop/공유할것/dstat_MG_D_64.txt", 'r')

ff = open('C:/Users/Slayer/Desktop/공유할것/dstat_MG_D_64_변수제거 선처리.csv', 'wt',newline='', encoding='utf-8')

wr = csv.writer(ff)
frist = csv.DictWriter(ff,['<-------------','_---------------total cpu usage----------------------->','','','','','<-----dsk/total----->','','<---paging stat--->','','<---------load stat--------->','','','<-------------memory stat---------------->','','','','<total network stat>','','<---------process stat-------->','','','<------i/o stat------>','','<---swap stat--->','','<-----system----->','','<-----system----->'])
frist.writeheader()


csvout = csv.DictWriter(ff,['usr','sys', 'idl', 'wai', 'hiq', 'siq', 'read', 'writ', 'in', 'out', '1m', '5m', '15m', 'used', 'buff', 'cach', 'free', 'recv', 'send', 'run', 'blk', 'new', 'read', 'writ', 'used', 'free', 'day','time', 'int', 'csw'])
csvout.writeheader()


def split(text):
    cleaned_text = re.sub('\|', ' ', text)
    cleaned_text = re.sub('         ', ',', cleaned_text)
    cleaned_text = re.sub('        ', ',', cleaned_text)
    cleaned_text = re.sub('       ', ',', cleaned_text)
    cleaned_text = re.sub('      ', ',', cleaned_text)
    cleaned_text = re.sub('     ', ',', cleaned_text)
    cleaned_text = re.sub('    ', ',', cleaned_text)
    cleaned_text = re.sub('   ', ',', cleaned_text)
    cleaned_text = re.sub('  ', ',', cleaned_text)
    cleaned_text = re.sub(' ', ',', cleaned_text)
    cleaned_text = re.sub('\\n', ',', cleaned_text)
    return cleaned_text

def clean_text(text):
    cleaned_text = re.sub('k', '', text)
    cleaned_text = re.sub('M', '', cleaned_text)
    cleaned_text = re.sub('B', '', cleaned_text)
    return cleaned_text
stack = 1

def K_text(text):
    count = text.count('k')
    if count == 0:
        pass
    else:
        text = re.sub('k', '', text)
        text = int(text)
        text = text*1000
    return text

#14~18,25,28~29*1000

while True:
    line = f.readline()
    if not line: break
    if (stack > 2):
        list_out = []
        a = []
        line = split(str(line))
        for i in range(1,31):
            b = line.split(',')[i]
            a.append(b)
        # 뒤에 붙은 k, M, B를 제거함
        a[14] = clean_text(a[14])
        a[15] = clean_text(a[15])
        a[16] = clean_text(a[16])
        a[17] = clean_text(a[17])
        a[18] = clean_text(a[18])
        a[25] = clean_text(a[25])

        a[28] = K_text(a[28])
        a[29] = K_text(a[29])

        list_out.append({'usr':a[0],'sys':a[1], 'idl':a[2], 'wai':a[3], 'hiq':a[4], 'siq':a[5], 'read':a[6], 'writ':a[7], 'in':a[8], 'out':a[9], '1m':a[10], '5m':a[11], '15m':a[12], 'used':a[13], 'buff':a[14], 'cach':a[15], 'free':a[16], 'recv':a[17], 'send':a[18], 'run':a[19], 'blk':a[20], 'new':a[21], 'read':a[22], 'writ':a[23], 'used':a[24], 'free':a[25], 'day':a[26],'time':a[27], 'int':a[28], 'csw':a[29]})
        csvout.writerows(list_out)
    else:
        stack = stack + 1

f.close()
