import csv

ff = open('C:/Users/Slayer/Desktop/공유할것/선처리_mg.csv', 'wt',newline='', encoding='utf-8')
wr = csv.writer(ff)

csvout = csv.DictWriter(ff,['cpu','sys' ,'inter_up','inter_down','ctxsw_up','ctxsw_down',\
                            'KBWrit','Writes','KBIn_up','KBIn_down','KBIn_same','PktIn_up','PktIn_down',\
                            'PktIn_same','KBOut','PktOut'])
csvout.writeheader()

f_r = open('C:/Users/Slayer/Desktop/공유할것/작업할것mg.csv', 'r', encoding='utf-8')
rdr = csv.reader(f_r)

before_inter = 0
now_inter = 0
before_ctxsw = 0
now_ctxsw = 0
before_KBIn_up_down = 0
now_KBIn_up_down = 0
before_PktIn_up_down = 0
now_PktIn_up_down = 0
stack = 0
for line in rdr:
    inter_up = 0
    inter_down = 0
    ctxsw_up = 0
    ctxsw_down = 0
    KBIn_up = 0
    KBIn_down = 0
    KBIn_same = 0
    PktIn_up = 0
    PktIn_down = 0
    PktIn_same = 0
    list_out = []
    before_inter = now_inter
    before_ctxsw = now_ctxsw
    before_KBIn_up_down = now_KBIn_up_down
    before_PktIn_up_down = now_PktIn_up_down
    if stack<2:
        stack = stack + 1
        before_inter = line[2]
        now_inter = line[2]
        before_ctxsw = line[3]
        now_ctxsw = line[3]
        before_KBIn_up_down = line[6]
        now_KBIn_up_down = line[6]
        before_PktIn_up_down = line[7]
        now_PktIn_up_down = line[7]
    else:
        now_inter = line[2]
        now_ctxsw = line[3]
        now_KBIn_up_down = line[6]
        now_PktIn_up_down = line[7]

        # 현재값이 전보다 클 경우
        if now_inter > before_inter:
            inter_up = 1
        elif now_inter <= before_inter:
            inter_down = 1
        # 현재값이 전보다 클 경우
        if now_ctxsw > before_ctxsw:
            ctxsw_up = 1
        elif now_ctxsw <= before_ctxsw:
            ctxsw_down = 1

        if now_KBIn_up_down > before_KBIn_up_down:
            KBIn_up = 1
        elif now_KBIn_up_down < before_KBIn_up_down:
            KBIn_down = 1
        else:
            KBIn_same = 1

        if now_PktIn_up_down > before_PktIn_up_down:
            PktIn_up = 1
        elif now_PktIn_up_down < before_PktIn_up_down:
            PktIn_down = 1
        else:
            PktIn_same = 1

        line[4] = int(line[4])
        line[5] = int(line[5])
        line[8] = int(line[8])
        line[9] = int(line[9])

        if line[4]>0:
            line[4] = 1
        else:
            line[4] = 0
        if line[5]>0:
            line[5] = 1
        else:
            line[5] = 0
        if line[8]>0:
            line[8] = 1
        else:
            line[8] = 0
        if line[9]>0:
            line[9] = 1
        else:
            line[9] = 0

        list_out.append({'cpu': int(line[0]), 'sys': int(line[1]), 'inter_up': int(inter_up),'inter_down': int(inter_down),\
                         'ctxsw_up': int(ctxsw_up),'ctxsw_down': int(ctxsw_down),'KBWrit': int(line[4]), 'Writes': int(line[5]),\
                         'KBIn_up':int(KBIn_up),'KBIn_down':int(KBIn_down),'KBIn_same':int(KBIn_same),'PktIn_up': int(PktIn_up),'PktIn_down': int(PktIn_down),'PktIn_same': int(PktIn_same),'KBOut': int(line[8]),\
                        'PktOut': int(line[9])})
        csvout.writerows(list_out)

ff.close()
f_r.close()