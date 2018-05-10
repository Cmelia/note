# -*- coding: utf-8 -*-
"""
def checkio(result):
    for i in range(3):
        if result[i][0]==result[i][1]:
            if result[i][1]==result[i][2]:
                return result[i][0]
        elif result[0][i]==result[1][i]:
            if result[1][i]==result[2][i]:
                return result[0][i]
        elif result[0][0]==result[1][1]==result[2][2]:
            return result[0][0]
        elif result[0][2]==result[1][1]==result[2][0]:
            return result[0][2]
        else:
            return "D"
"""


# 方法二
def checkio(game_result:list)-> str:
    rows = game_result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
