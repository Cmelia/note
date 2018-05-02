# -*- coding:utf-8 -*-
import re
# 使用\d{1,3}匹配每行中1-999的数据，不能以0开头
test_str='''
1
10
100
999
1000
01
001
'''

# 预期：匹配
# 1
# 10
# 100
# 999


# 不会用\d{1，3}实现啊。。。
# words=test_str.split()
# for word in words:
#     pattern=re.compile(r'^[1-9]\d{0,2}$')
#     if pattern.search(word):
#         print word

# c
pattern = re.compile(r'^(?!^0.*)\d{1,3}$')
for s in test_str.split():
    if pattern.match(s):
        print(s)
