#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给你一个字符串格式的正数和一个小于37大于1的整数型底数，用你写出来的方法来把他们转换为底数为10（十进制）的形式。 任务使用数字和‘A-Z’来作为字符串格式的正数。

注意数字无法转换的情况。 例如：“1A”不能用基数9进行转换。对于这些情况，你的函数应该返回-1。

输入: 两个参数，一个字符串参数的正数和一个整数参数底数。

输出: 一个被转换完的十进制整数。

checkio("AF", 16) == 175
checkio("101", 2) == 5
checkio("101", 5) == 26
checkio("Z", 36) == 35
checkio("AB", 10) == -1
Precondition:
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ≤ 10
2 ≤ radix ≤ 36
"""
__author__ = "Ysara"


def checkio(str_number, radix):
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")