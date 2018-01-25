#coding=utf-8
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print fib(36)


def Rabbit(num):
    i = 1
    a, b = 1, 1
    while i <= num:
        yield a
        i += 1
        a, b = b, a + b


list = [x for x in Rabbit(4)]
print(list)