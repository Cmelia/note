# -*- coding:utf-8 -*-
import re
'''
(the|The|THE)
(t|T)h(e|eir)

\b[tT]h[ceinry]*\b
'''
list1=['the','The','THE','Their','thi','tha']
pattern=re.compile(r'\b([tT][hH])([Eceinry]*|eir)\b')
for l in list1:
    if pattern.search(l):
        print l
