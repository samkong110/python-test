# coding=utf-8
# @Time    : 2018/1/18 9:33
# @Author  : Jiangxu
# @File    : 阶乘.py
# @Software: PyCharm

n = int(raw_input('请输入计算个数'))
s = 0
t = 1
for n in range(1,n+1):
    t *= n
    s += t

print s





