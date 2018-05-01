# -*- coding:utf-8 -*-
# 需求：将每行特定格式数据格式化为SQL语句

import re

string='''
1 2017-04-11 Zjmainstay
2 2017-04-12 Nobody
3 2017-04-13 Somebody
'''
words=string.split('\n')
pattern=re.compile(r'(\d)\s([\d\-]{2,})\s([a-zA-Z]{1,})')
for word in words:

    g=pattern.search(word)
    if g:
        print(re.sub(pattern,"INSERT INTO table_log(`id`, `created_at`, `author`)values('"+g.group(1)+"', '"+g.group(2)+"', '"+g.group(3)+"');",word))
