
"""
给你一个其中包含不同的英文字母和标点符号的文本，你要找到其中出现最多的字母，返回的字母必须是小写形式，
当检查最想要的字母时，不区分大小写，所以在你的搜索中 "A" == "a"。 请确保你不计算标点符号，数字和空格，只计算字母。

如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母。 例如 -- “one”包含“o”，“n”，“e”每个字母一次，因此我们选择“e”。

输入: 用于分析的文本.

输出: 最常见的字母的小写形式。

范例:
checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"

如何使用： 对于大多数的解密任务，你需要知道各种字母出现在一段文字的频率。例如：如果我们知道在哪个字母出现的频率，我们可以很容易地破解一个简单的加法密码或替换密码。这是语言专家有趣的事情！

前提::
密码只包含ASCII码符号
0 < len(text) ≤ 105

"""

def checkio(text):
    
    # your answer
    pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")