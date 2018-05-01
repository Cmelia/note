# -*- coding:utf-8 -*-
import re
#需求：分组1得到每行链接中的文件名
string='''
http://localhost.com/a/b/c/d/file1.txt
https://localhost.com/a/b/file2long.jpg
'''

words=string.split()
for word in words:
    pattern=re.compile(r'zhengze2.py')
