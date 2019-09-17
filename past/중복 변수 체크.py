import re

name_csv_collectl = [
    'usr','sys','idl','wai','hiq','siq',
    'read','writ',
    'recv','send',
    'in','out',
    'int','csw',
    'run','blk','new',
    'used','buff','cach','free',
    'used','free',
    '1m','5m','15m',
    'read','writ',
    '#aio',
    'files','inodes',
    'msg', 'sem','shm',
    'pos','lck','rea','wri',
    'raw',
    'tot','tcp','udp','raw','frg',
    'lis','act','syn','tim','clo',
    'lis','act',
    'dgm','str','lis','act',
    'majpf','minpf','alloc','free',
    'epoch'
]
"""
1번째줄 (usr ~ siq)  : total-cpu-usage
2번째줄 (read ~ writ): dsk/total
3번째줄 (recv ~ send)  : net/total
4번째줄 (in ~ out) : paging
5번째줄 (int ~ csw) : system
6번째줄 (run ~ new) : procs
7번째줄 (used ~ free) : memory-usage
8번째줄 (used ~ free) : swap
9번째줄 (1m ~ 15m) : load-avg
10번째줄 (read ~ writ) : io/total
11번째줄 (#aio)  : async
12번째줄 (files ~ inodes): filesystem
13번째줄 (msg ~ shm)  : sysv-ipc
14번째줄 (pos ~ wri) : file-locks
15번째줄 (raw) : raw
16번째줄 (tot ~ frg) : sockets
17번째줄 (lis ~ clo) : tcp-sockets
18번째줄 (lis ~ act) : udp
19번째줄 (dgm ~ act) : unix-sockets
20번째줄 (majpf ~ free) : virtual-memory
21번째줄 (epoch) : epoch
"""

for i in range(0,119):
    for k in range(i+1,119):
        if name_csv_collectl[i] == name_csv_collectl[k]:
            print(name_csv_collectl[i])