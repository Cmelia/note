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


# c
def get_first_from_sorted(args, key, reverse):
    args = args[0] if len(args) == 1 else args
    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return get_first_from_sorted(args, key, False)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")