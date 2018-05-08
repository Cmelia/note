# -*- coding:utf-8 -*-
import re
"""
找到其中出现最多的字母，返回的字母必须是小写形式，
请确保你不计算标点符号，数字和空格，只计算字母。
前提:
密码只包含ASCII码符号
0 < len(text) ≤ 105

"""

# 方法一：26个字母，每个都统计一遍不管出现还是不出现
def checkio(text):
    num = 0
    maxn = 0
    maxs='a'
    for i in range(26):
        s= chr(i + ord('a'))
        temp = num
        textlow=text.lower()
        num = textlow.count(s)
        if num>maxn:
            maxn=num
            maxs=s

    return maxs


# 方法二：哪个字母出现就统计哪个字母
def isletter(text):
    pattern = re.compile(r'[a-zA-Z]')
    ss = ''
    for s in text:
        if pattern.search(s):
            ss = s + ss
    sslow=ss.lower()[::-1]
    sslow=sorted(sslow)
    return sslow
def checkio(text):
    a = isletter(text)

    l=[]
    for i in a:
        num=a.count(i)
        l.append(num)
    ind=l.index(max(l))
    return a[ind]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
