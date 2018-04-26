# regular expression

## 验证输入是否是汉字

## 需求：匹配每行数据中以.jpg/.jpeg/.png/.gif结尾的图片名称（含后缀）

```shell
数据:

image.jpg
image.jpeg
image.png
image.gif
not_image.txt
not_image.doc
not_image.xls
not_image.ppt
```

## 需求：匹配由 A/S/D/F 4个字母(区分大小写)组成的长度为3字符串

```shell
ABC
ASD
ADS
ASF
BBC
A|S
A|D
ASDF
```

## 需求：匹配连续相同3次的数字

```shell
111
121
112
222
```

## 需求：校验密码必须包含字母、数字和特殊字符，6-16位，假定特殊字符为 -_= 三个字符

```shell
12345
123456
1234561234561234
12345612345612345
a1234
a12345
-1234
-12345
a-123
a-1234
a-1234a-1234a-12
a-1234a-1234a-1234
aaaaa
aaaaaa
-_=-_
-_=-_=
```

## 需求：使用\d{1,3}匹配每行中1-999的数据，不能以0开头

```shell
1
10
100
999
1000
01
001
预期：匹配
1
10
100
999
```

## 需求：分组1得到每行链接中的文件名

```shell
http://localhost.com/a/b/c/d/file1.txt
https://localhost.com/a/b/file2long.jpg
```

## 表达式

```shell
(the|The|THE)
(t|T)h(e|eir)

\b[tT]h[ceinry]*\b

```
