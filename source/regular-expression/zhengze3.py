# -*- coding:utf-8 -*-

#匹配连续相同3次的数字

import re

string='''
111
121
112
222
'''

words=string.split()

for word in words:
    pattern=re.compile(r'([0-9])\1\1')
    if pattern.search(word):
        print word

