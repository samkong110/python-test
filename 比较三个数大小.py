#coding=utf-8
# x = int (raw_input('输入x'))
# y = int (raw_input('输入y'))
# z = int (raw_input('输入z'))
# if x<y:
#     if y<z:
#         print x,y,z
#     if y>z:
#         if x < z:
#             print x,z ,y
#         else:
#             print z,x,y
# if x > y:
#     if y > z:
#         print z,y,x
#     if y < z:
#         if x > z:
#             print x,z,y
#         else:
#             print z,x,y
list = []

for i in range(3):
    i +=1
    num = int(raw_input('请输入第%d个值'%i))
    list.append(num)
list.sort()
print list



