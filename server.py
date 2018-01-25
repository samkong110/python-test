# coding=utf-8
# @Time    : 2018/1/19 14:38
# @Author  : Jiangxu
# @File    : server.py
# @Software: PyCharm
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    print '连接地址： ',addr
    c.send('Hello Python Socket')
    c.close()


