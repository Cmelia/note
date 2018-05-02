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

# ^(?!([a-zA-Z\d]*|[a-zA-Z\-_=]*|[\d\-_=]*)$)[a-zA-Z\d\-_=]{6,16}$

# (?!pattern)
# 非获取匹配，正向否定预查，在任何不匹配pattern的字符串开始处匹配查找字符串，
# 该匹配不需要获取供以后使用。例如“Windows(?!95|98|NT|2000)”能匹配“Windows3.1”
# 中的“Windows”，但不能匹配“Windows2000”中的“Windows”。