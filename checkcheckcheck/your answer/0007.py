# -*- coding:utf-8 -*-


def min(*args, **kwargs):
    if args!=None:
        print(args,'111')
        min=args[0]
        for i in range(len(args)-1):
            if args[i+1]<min:
                min=args[i+1]
    if kwargs!=None:
        print(kwargs)
        min=kwargs[0]
        for i in range(len(kwargs) - 1):
            if kwargs[i + 1] < min:
                min = kwargs[i + 1]

    return min




def max(*args, **kwargs):
    key = kwargs.get("key", None)
    return 0


l=min([1,2,3,2])
print(l)