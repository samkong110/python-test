# coding=utf-8
# @Time    : 2018/1/18 9:11
# @Author  : Jiangxu
# @File    : 分数序列求和.py
# @Software: PyCharm

a = 2.0
b = 1.0
l = []

for i in range(20):
    l.append(a / b)
    t = a
    a = a + b
    b = t
print sum(l)


