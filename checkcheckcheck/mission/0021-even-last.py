#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给你一个整数数组，需要你把具有偶数索引的元素相加（0，2，4 ...），然后把相加后得到的数与最后一个元素相乘。 不要忘记，第一个元素的索引是0。

如果传入的是一个空数组，则应该返回0。

输入: 一个整数列表

输出: 你得出的答案（整数值类型）

前提条件: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""
__author__ = "Ysara"


def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """

    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")