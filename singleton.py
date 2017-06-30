#!/usr/bin/env python 
#-*- coding: UTF-8 -*- 


''' 
#Module: singleton
#Created by Leo Wen on 2017-06-03 13:56:44
''' 
import os 
import sys 
import datetime 
import re 

'''
所谓单例模式就是一个类只能创建一个实例化
1. 继承类的方法，类中定义只创建一次实例
通过__new__方法，将类的实例在创建的时候绑定到类属性_inst上。如果cls._inst为None，说明类还未实例化，实例化并将实例绑定到cls._inst，以后每次实例化的时候都返回第一次实例化创建的实例。注意从Singleton派生子类的时候，不要重载__new__。
'''
class singleton(object):
	def __new__(cls,*args,**kw):
		if not hasattr(cls,'_instance'): 
			cls._instance = super(singleton,cls).__new__(cls,*args,**kw)
		return cls._instance

class hello(singleton): #继承
#class hello():
	#__metaclass__ = singleton		#元类
	def __init__(self,s):
		self.s = s
		print 'hello: ',self.s

def test(): 
	a = hello('apple')
	b = hello('banana')
	print id(a),a.s
	print id(b),b.s

'''
2. 可以使用导入模块方式
python中的模块module在程序中只被加载一次，本身就是单例的。可以直接写一个模块，将你需要的方法和属性，写在模块中当做函数和模块作用域的全局变量即可，根本不需要写类。
'''

'''
3. 最简单的方法：将类自己实例化
将名字singleton绑定到实例上，singleton就是它自己类的唯一对象了。
'''
class singleton(object):
  pass
singleton=singleton()


'''
4. 使用装饰器，decorator

'''
def singleton1(cls,*args,**kw):
	instances = {}
	def _singleton():
		if cls not in instances:
			instances[cls] = cls(*args,**kw)
		return instances[cls]
	return _singleton

@singleton1
class myClass1(object):
	a = 1
	def __init__(self,x=0):
		self.x = x

def test1():
	a = myClass1()
	b = myClass1()
	b.a = 3 
	print id(a), a.x,a.a
	print id(b), b.x,b.a
	print b == a
	





if __name__ == '__main__': 
	#test() 
	test1()


