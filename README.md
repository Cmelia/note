# 练习

## 简答题

[简答题](./简答题.md)

## code

所有的代码均放置在 `source` 目录下以题目序号命名的目录里.

例如: `source/0003`

### 0001. 幸运时间

![jd-01](/assets/jd-01.jpeg)

### 0002. 生成一个100行内容的的文件, 做文件拆分, 写到10个文件, 每个文件10行

### 0003. 对里面的单词进行统计

```shell
# 获取测试文件
wget https://github.com/Cmelia/note/blob/changlangyue/assets/The%20Old%20Man%20and%20the%20Sea.txt
```

### 0004. 字符串处理

![alt](/assets/hanshu.jpg)

### 0005 文件处理

![alt](/assets/wenjian.jpeg)

### 0006. Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits

Input: A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.
checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

```python
def checkio(data):

    #replace this for solution
    return True or False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
 print("done")
```

### 0007. You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string.

```python
def checkio(text):

    #replace this for solution
    return 'a'

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
```

### 0008. 整数分解

![jd-02](/assets/jd-02.jpeg)
