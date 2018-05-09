# -*- coding:utf-8 -*-

"""
给你一个非空列表, 返回在此列表中的非唯一元素的列表。
要做到这一点，你需要删除所有给定的列表只有一次的元素。
解决这个任务时，不能改变列表的顺序。
例如：[1，2，3，1，3] 1和3是非唯一元素，结果将是 [1, 3, 1, 3]。
"""
# 方法一
def checkio(data):
    datacopy=data[:]
    for i in data:
        num=data.count(i)
        if num==1 :
            datacopy.remove(i)
    return datacopy

# 方法二
def checkio(data):
    return [i for i in data if data.count(i)>1]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

