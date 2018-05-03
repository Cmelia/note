# -*- coding:utf-8 -*-

#匹配每行数据中以.jpg/.jpeg/.png/.gif结尾的图片名称（含后缀
import re

string='''image.jpg image.jpeg image.png
    image.gif not_image.txt not_image.doc
    not_image.xls not_image.ppt'''

words=string.split()

for word in words:
    #print word
    pattern=r'(.jpg)$|(.jpeg)$|.png$|.gif'
    if re.search(pattern,word):
        print word

#方法二
s = """
image.jpg
image.jpeg
image.png
image.gif
not_image.txt
not_image.doc
not_image.xls
not_image.ppt
"""

postfix = ('jpg', 'jpeg','png', 'gif')

print(list(x for x in s.split() if x.split('.')[1] in postfix ))

