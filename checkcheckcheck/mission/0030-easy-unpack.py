#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
在这里你的任务是创建得到一个元组，并返回一个包含三个元素（第一，第三和倒数第二的给定元组）的元组与的功能。

输入: 一个不少于三个元素的元组

输出: 一个元组.
"""
__author__ = "Ysara"


def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """

    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
