import re
import openpyxl
import csv

ff = open('C:/Users/Slayer/Desktop/20180801 모니터링 정보 (1)/collectl_output_EP_D_64.csv', 'wt',newline='', encoding='utf-8')
wr = csv.writer(ff)
# ws = wb.get_sheet_by_name("Sheet1")
stack = 0
i = 3
list_out = []

frist = csv.DictWriter(ff,[' ','','<-------------------CPU------------------->','','','','<-----------------Disks------------------->','','','','<-----------------Networks---------------->','',''])
frist.writeheader()


csvout = csv.DictWriter(ff,['Date','Time','cpu','sys' ,'inter','ctxsw','KBRead','Reads','KBWrit','Writes','KBIn','PktIn','KBOut','PktOut'])
csvout.writeheader()



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

f = open("C:/Users/Slayer/Desktop/20180801 모니터링 정보 (1)/collectl_output_EP_D_64.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    if (stack > 2):
        list_out = []
        a = []
        line = split(str(line))
        print(str(line))
        for i in range(0,14):
            b = line.split(',')[i]
            a.append(b)
        print(a)
        list_out.append({'Date':a[0], 'Time':a[1], 'cpu':a[2], 'sys':a[3], 'inter':a[4], 'ctxsw':a[5], 'KBRead':a[6], 'Reads':a[7], 'KBWrit':a[8], 'Writes':a[9], 'KBIn':a[10],'PktIn':a[11], 'KBOut':a[12],'PktOut':a[13]})
        csvout.writerows(list_out)

    if (stack == 24):
        stack = 1
        print("=========================")
    else:
        stack = stack + 1

    j=0
    i = i + 1
f.close()

