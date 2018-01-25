# coding=utf-8
# @Time    : 2018/1/18 10:57
# @Author  : Jiangxu
# @File    : 递归.py
# @Software: PyCharm

def age(n):
    if n == 1: c = 10
    else: c = age(n - 1) + 2
    return c
print age(5)

s = raw_input('输入一个值')
print len(s)
s=s[::-1]
for i in s:
    print i