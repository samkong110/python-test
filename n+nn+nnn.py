#coding=utf-8
a = int(raw_input('请输入数字：'))
n = int(raw_input('请输入相加次数：'))
l = []
for i in range(n):
    s = 0 + a*pow(10,i)
    l.append(s)
t = l[0]
while len(l)>1:
    t += sum(l)
    l.pop()

print t


