#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
'''
#Module name:testnewclass.py
#Created by Leo Wen  
'''
import os
import sys

'''
新式类是广度优先,旧式类是深度优先

类和类型是不同的，如a是ClassA的一个实例，那么a.__class__返回 ‘ class    __main__.ClassA‘ ，type(a)返回总是<type 'instance'>。而引入新类后，比如ClassB是个新类，b是ClassB的实例，b.__class__和type(b)都是返回‘class '__main__.ClassB' ，这样就统一了。

新类：为了统一类(class)和类型(type)。
在Python3里面，不存在这些问题了，因为所有的类都是object类的子类（隐式）
为了向前兼容，默认情况下用户定义的类为经典类，新类需要继承自所有类的基类 object 或者继承自object的新类。
'''

class oldClass():	#经典类，旧式类
	def __init__(self):
		pass

class newClass(object):		#新类
	def __init__(self):
		pass

def test1():
	c1 = oldClass()
	c2 = newClass()
	print c1.__class__
	print type(c1)
	print c2.__class__
	print type(c2)
	'''
	__main__.oldClass
	<type 'instance'>
	<class '__main__.newClass'>
	<class '__main__.newClass'>
	'''


'''
动态的创建类：
利用函数
type
'''
def choose_class(name):
	if name == 'foo':
		class Foo(object):
			pass
		return Foo     # 返回的是类，不是类的实例
	else:
		class Bar(object):
			pass
		return Bar

def test2():
	MyClass = choose_class('foo')
	print MyClass	 # 函数返回的是类，不是类的实例
	print MyClass()   # 你可以通过这个类创建类实例，也就是对象
	
def testtype():
	#type可以查看对象的类型
	print type(1)
	print type('1')
	print type([1])

'''
元类就是用来创建这些类（对象）的，元类就是类的类
__metaclass__ = type

元类的主要目的就是为了当创建类时能够自动地改变类

通过在模块级别设定__metaclass__。采用这种方法，这个模块中的所有类都会通过这个元类来创建，我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。
'''
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
	'''返回一个类对象，将属性都转为大写形式'''
	# 选择所有不以'__'开头的属性
	attrs = ((name, value) for name, value in future_class_attr.items())
	#将它们转为大写形式
	uppercase_attr=dict((name.upper(), value) for name, value in attrs)
 
	#通过'type'来做类对象的创建
	return type(future_class_name, future_class_parents, uppercase_attr)
 
#__metaclass__ = upper_attr  #  这会作用到这个模块中的所有类

#__metaclass__ 需要设定在类中，作用域整个类
class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
	__metaclass__ = upper_attr
	bar = 'bip'

def test3():
	print hasattr(Foo, 'bar')
	print hasattr(Foo, 'BAR')
	f = Foo()
	print f.BAR


if __name__ == "__main__":
	test3()
