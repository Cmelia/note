#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ysara"

"""
找到字符串中最长的相同字符重复出现的次数，并返回它的重复次数。

例如：字符串“aaabbcaaaa”包含具有相同字母“aaa”，“bb”，“c”和“aaaa”的四个子字符串。 
最后一个子字符串是最长的一个字符串，你应该返回 4 。

输入: 一个字符串.

输出: 一个整数.
"""


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """

    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')