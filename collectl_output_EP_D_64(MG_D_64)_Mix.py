import re
import csv

ff = open('C:/Users/Slayer/Desktop/공유할것/collectl_output_Mixx.csv', 'wt',newline='', encoding='utf-8')
wr = csv.writer(ff)
# ws = wb.get_sheet_by_name("Sheet1")
stack = 0
i = 3
list_out = []

csvout = csv.DictWriter(ff,['time_ep','time_mg','ep','mg'])
csvout.writeheader(),

f_1 = open("C:/Users/Slayer/Desktop/공유할것/collectl_output_EP_D_64.txt", 'r')

f_2 = open("C:/Users/Slayer/Desktop/공유할것/collectl_output_MG_D_64.txt", 'r')

count = 1
pool = 0

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

while True:
    line_1 = f_1.readline()
    line_2 = f_2.readline()
    if (count > 158): break
    if pool < 7:
        pool = pool + 1
    else:
        print("t실행")
        if (stack > 2):
            print()
            list_out = []
            a_1 = 0
            a_2 = 0
            b_1 = 0
            b_2 = 0
            b_4 = 0
            b_5 = 0

            line_1 = split(str(line_1))
            line_2 = split(str(line_2))
            b_0 = line_1.split(',')[1]
            b_1 = line_1.split(',')[4]
            b_2 = line_1.split(',')[5]
            b_3 = line_2.split(',')[1]
            b_4 = line_2.split(',')[4]
            b_5 = line_2.split(',')[5]
            b_1 = int(b_1)
            b_2 = int(b_2)
            b_4 = int(b_4)
            b_5 = int(b_5)
            a_1 = round(b_2/b_1,5)
            a_2 = round(b_5/b_4,5)
            a_1 = a_1 * 100
            a_2 = a_2 * 100

            list_out.append({'time_ep':b_0,'time_mg':b_3,'ep':a_1 , 'mg':a_2})
            csvout.writerows(list_out)

    if (stack == 23):
        stack = 0
        print("=========================")
    else:
        stack = stack + 1

    i = i + 1
    count = count + 1
f_1.close()
f_2.close()