# coding=utf-8
# @Time    : 2018/1/19 14:18
# @Author  : Jiangxu
# @File    : python正则表达式.py
# @Software: PyCharm
import re
m = re.search(r'^\d{3}\-\d{3,8}$', '010-12345')
print m.group(0)

print 'a b   c'.split(' ')

l = re.split(r'\s+','a, b;;   c')
ll = re.split(r'[\s,;]+','a, b;;   c')
print l
print ll