#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
斯蒂芬和索菲亚对于一切都使用简单的密码，忘记了安全性。请你帮助尼古拉开发一个密码安全检查模块。如果密码的长度大于或等于10个字符，且其中至少有一个数字、一个大写字母和一个小写字母，该密码将被视为足够强大。密码只包含ASCII拉丁字母或数字。

输入: 密码。

输出: 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值的数据类型。你会在结果看到转换后的结果(True 或 False)。

范例:

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

如何使用: 如果你担心你的应用或服务的安全性，您可以检查用户密码的复杂性。你可以使用这些技巧要求你的用户的密码符合多个条件（标点符号或unicode）。

前提: 
re.match("[a-zA-Z0-9]+", password) 
0 < len(password) ≤ 64
"""

def checkio(data):
    
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