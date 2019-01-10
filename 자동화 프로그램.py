import csv
import re

name = "'usr','sys','idl','wai','hiq','siq',\
    'read','writ',\
    'recv','send',\
    'in','out',\
    'int','csw',\
    'run','blk','new',\
    'used','buff','cach','free',\
    'used','free',\
    '1m','5m','15m',\
    'read','writ',\
    '#aio',\
    'files','inodes',\
    'msg', 'sem','shm',\
    'pos','lck','rea','wri',\
    'raw',\
    'tot','tcp','udp','raw','frg',\
    'lis','act','syn','tim','clo',\
    'lis','act',\
    'dgm','str','lis','act',\
    'majpf','minpf','alloc','free',\
    'epoch'"
def split(text):
    cleaned_text = re.sub('                   ', ',', text)
    cleaned_text = re.sub('                  ', ',', cleaned_text)
    cleaned_text = re.sub('                 ', ',', cleaned_text)
    cleaned_text = re.sub('                ', ',', cleaned_text)
    cleaned_text = re.sub('               ', ',', cleaned_text)
    cleaned_text = re.sub('              ', ',', cleaned_text)
    cleaned_text = re.sub('             ', ',', cleaned_text)
    cleaned_text = re.sub('            ', ',', cleaned_text)
    cleaned_text = re.sub('           ', ',', cleaned_text)
    cleaned_text = re.sub('          ', ',', cleaned_text)
    cleaned_text = re.sub('         ', ',', cleaned_text)
    cleaned_text = re.sub('        ', ',', cleaned_text)
    cleaned_text = re.sub('       ', ',', cleaned_text)
    cleaned_text = re.sub('      ', ',', cleaned_text)
    cleaned_text = re.sub('     ', ',', cleaned_text)
    cleaned_text = re.sub('    ', ',', cleaned_text)
    cleaned_text = re.sub('   ', ',', cleaned_text)
    cleaned_text = re.sub('  ', ',', cleaned_text)
    cleaned_text = re.sub(' ', ',', cleaned_text)
    return cleaned_text

name = name.count(',')
print(name)