# coding=utf-8
# @Time    : 2018/1/18 10:43
# @Author  : Jiangxu
# @File    : 回文数判断.py
# @Software: PyCharm

s = raw_input('输入一个五位数')
if s[0]==s[-1] and s[1]==s[-2]:
    print True
else:
    print False
