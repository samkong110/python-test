#coding=utf-8

i = int(raw_input(u"请输入利润总额： 万元！"))
'''
if i <=10:
    b= i*0.1
    print b
elif 10<i<=20:
    b= 10*0.1+(i-10)*0.075
    print b
elif 20<i<=40:
    b= 10*0.1 + 10 * 0.075 + (i-20)*0.05
    print b
elif 40<i<=60:
    b= 10*0.1 + 10 * 0.075 + 20*0.05 + (i-40)*0.03
    print b
elif 60<i<=100:
    b= 10*0.1 + 10 * 0.075 + 20*0.05 + 20*0.03 + (i-60)*0.015
    print b
else:
    b= 10*0.1 + 10 * 0.075 + 20*0.05 + 20*0.03 + 40*0.03 + (i-60)*0.01
    print b
'''
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for n in range (0,6):
    if i > arr[n]:
        r += (i-arr[n])*rat[n]
        print (i-arr[n])*rat[n]
        i = arr[n]
print r



