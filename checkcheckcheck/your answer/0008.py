# -*- coding: utf-8 -*-


"""
找到字符串中最长的相同字符重复出现的次数，并返回它的重复次数。
"""


def long_repeat(text):
    if text=='':
        return 0
    else:
        c=[]
        for i in text:
            count=0
            t=i

            while(text.find(t)!=-1):
                count+=1
                t=t+i

            c.append(count)
        l=max(c)
        return l


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
