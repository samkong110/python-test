#coding=utf-8
import time


print time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)
data = '2000/12/22'
print time.strptime(data,'%Y/%m/%d')