# coding=utf-8
# @Time    : 2018/1/17 17:10
# @Author  : Jiangxu
# @File    : 乒乓球.py
# @Software: PyCharm
# 范例
for a in ['x','y','z']:
    for b in ['x', 'y', 'z']:
        for c in ['x', 'y', 'z']:
            if(a!=b)and(b!=c)and(c!=a) and (a!='x') and (c!='x') and (c!='z'):
                print 'a和%s比赛，b和%s比赛，c和%s比赛' %(a,b,c)