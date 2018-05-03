# -*- coding:utf-8 -*-

#匹配由 A/S/D/F 4个字母(区分大小写)组成的长度为3字符串

import re

string='''
ABC
ASD
ADS
ASF
BBC
A|S
A|D
ASDF
'''
words=string.split()
for word in words:
    pattern=re.compile(r'\b[ASDF]{3}\b')
    if pattern.search(word):
        print word

l1=list(x for x in string.split() if len(x)==3 )




