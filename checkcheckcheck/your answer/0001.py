# -*- coding:utf-8 -*-

'''如果密码的长度大于或等于10个字符，且其中至少有一个数字、一个大写字母和一个小写字母，
该密码将被视为足够强大。密码只包含ASCII拉丁字母或数字。
输入: 密码。
输出: 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值的数据类型。
你会在结果看到转换后的结果(True 或 False)。
'''
import re
# 判断是否包含字母数字大写
regexp=r'^(?!([a-zA-Z]*|[A-Z0-9]*|[0-9a-z]*)$)([a-z]+|[A-Z]+|[0-9]+)'

#不知道该如何判断密码只包含ASCII拉丁字母或数字。

def checkio(data):
    if len(data)>10:
        if re.search(regexp,data):
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('##########') == False
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

