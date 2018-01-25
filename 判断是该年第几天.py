#coding=utf-8


time = raw_input('输入年月日：')
#time = '20000301'
days=[31,59,90,120,151,181,212,243,273,304,334]
year = time[0:4]
m = time[4:6]
if int(m) == 10 or int (m) == 20:
    month = m
else:
    month = m.strip('0')

d = time[6:]
if int(d) == 10 or int (d) == 20:
    day = d
else:
    day = d.strip('0')

total = 0
if int(month) == 1:
    print day
if int(month) == 2:
    total = days[int(month) - 2] + int(day)
    print total
if int(month) > 2:
    if (int(year) % 400 == 0) or ((int(year) % 4 == 0) and (int(year) % 100 != 0)):
        total = 1 + days[int(month)-2] + int(day)
        print total
    else:
        total = days[int(month) - 2] + int(day)
        print total








