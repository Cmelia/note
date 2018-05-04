#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
你有一系列字符串，你要从中找出出现频率最高的字符串。

输入: 一个字符串组成的列表

输出: 一个字符串.
"""
__author__ = "Ysara"


def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')