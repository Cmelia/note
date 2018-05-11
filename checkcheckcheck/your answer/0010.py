# -*- coding:utf-8 -*-


def to_encrypt(text, delta):
    li=[]
    ss=str()
    for i in range(26):
        s = chr(i + ord('a'))
        li.append(s)
    for i in text:

        if i.isalpha():
            if li.index(i)+delta>26:
                b = li[li.index(i) + delta-26]
            else:
                b=li[li.index(i)+delta]
            #print(i,b)
            ss=ss+b
        else:
            ss=ss+' '



    return ss.rstrip()


a=to_encrypt("simple text", 16)
print(a.rstrip())


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
