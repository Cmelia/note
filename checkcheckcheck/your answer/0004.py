# -*- coding:utf-8 -*-
import re
'''
def count_words(text,words):
    text=text.split()
    textlist=[]
    for t in text:
        tword=''.join(tw for tw in t if tw.isalpha())
        textlist.append(tword)

    count=0
    for tl in textlist:
        for w in words:
            tll=tl.lower()
            tsp=tll.split(w)
            if len(tsp)==2:
                count+=1

    return count

'''


def count_words(text,words):
    count=0
    for w in words:
        if w in text.lower():
            count+=1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
