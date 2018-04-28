#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ysara"

"""
在给定的列表中检查是否所有元素全部相等。

输入: 列表

输出: 布尔值

例如:

all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True

前提: 输入的列表中的所有元素均是可哈希的。
"""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here

    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
