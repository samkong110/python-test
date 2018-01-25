# coding=utf-8
# @Time    : 2018/1/17 16:51
# @Author  : Jiangxu
# @File    : 猴子吃桃.py
# @Software: PyCharm

l = []
last = 1
for i in range(1,10,1):
    last = (last+1)*2
    l.append(last)

print l[-1]

