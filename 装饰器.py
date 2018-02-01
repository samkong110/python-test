# coding=utf-8
# @Time    : 2018/2/1 14:56
# @Author  : Jiangxu
# @File    : 装饰器.py
# @Software: PyCharm
import functools
# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args,**kw):
# 		print 'begin call'
# 		print 'call %s():' % func.__name__
# 		func(*args,**kw)
# 		print 'end call'
# 	print 'test'
# 	return wrapper

def log(*args):
	if callable(args[0]):
		func = args[0]
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'begin call'
			print 'call %s():' % func.__name__
			r =  func(*args,**kw)
			print 'end call'
			return r
		return wrapper
	else:
		t = args[0]
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print '%s %s():' % (t, func.__name__)
				return func(*args, **kw)
			return wrapper
		return decorator



@log('text')
def now():
	print '2018-02-01'

@log
def now1():
	print '2018-02-02'

now()
now1()


# now()
print now.__name__
#
# f = now
#
# f()
#
print now1.__name__
#
# print f.__name__