#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.

For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string.

Precondition: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)
"""
__author__ = "Ysara"


def find_message(text):
    """Find a secret message"""
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    assert find_message("dnwkldhiqw3ry37xhqdxaifiuoa7eya8w6r87a7y87y&Y&*DS&*DYH*&d8w9y8whd7*&Whdukjldwj*HDJKj") == "YDSDYHWHDJK"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")