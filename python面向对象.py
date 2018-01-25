# coding=utf-8
# @Time    : 2018/1/19 13:37
# @Author  : Jiangxu
# @File    : python面向对象.py
# @Software: PyCharm
class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print 'Toatal Employee %d' % Employee.empCount

    def displayEmployee(self):
        print 'name:',self.name, ',salary:',self.salary

class ChildEmployee(Employee):
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
    def displayChildEmployee(self):
        print 'name:', self.name, ',salary:', self.salary, ',age:', self.age

emp1 = Employee('Jack',2000)
emp2 = Employee('Lee',3000)
emp3 = ChildEmployee('Liu',4000,25)
emp3.displayChildEmployee()
emp3.displayCount()
emp3.displayEmployee()
emp1.age = 25
emp1.displayEmployee()
# del emp1.age
print hasattr(emp1,'age')
print getattr(emp1,'age')

emp2.displayEmployee()

emp2.displayCount()


