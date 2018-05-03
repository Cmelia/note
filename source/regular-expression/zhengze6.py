# -*- coding:utf-8 -*-
import re
#需求：分组1得到每行链接中的文件名
test_str='''
http://localhost.com/a/b/c/d/file1.txt
https://localhost.com/a/b/file2long.jpg
'''

# words=test_str.split()
# for word in words:
#     pattern=re.compile(r'zhengze2.py')

# c
pattern = re.compile(r'^.*/(.*$)')
for w in test_str.split():
    print(pattern.match(w).groups()[0])
