# -*- coding:utf-8 -*-
import re
#需求：校验密码必须包含字母、数字和特殊字符，
#6-16位，假定特殊字符为 -_= 三个字符

string='''
12345
123456
1234561234561234
12345612345612345
a1234
a12345
-1234
-12345
a-123
a-1234
a-1234a-1234a-12
a-1234a-1234a-1234
aaaaa
aaaaaa
-_=-_
-_=-_=
'''

words=string.split()

for word in words:
    pattern=re.compile(r'\b[0-9a-zA-z\-_=]+\b{6,16}')
    if pattern.search(word):
        print word
