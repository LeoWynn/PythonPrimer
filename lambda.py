#!/usr/bin/env python 
#-*- coding: UTF-8 -*- 


''' 
#Module: lambda
#Created by Leo Wen on 2017-06-03 15:42:23
''' 
import os 
import sys 
import datetime 
import re 


class lambda1(object): 
	def __init__(self): 
		pass 

'''
Python 允许你定义一种单行的小函数。
如果你的函数非常简单,只有一个表达式,不包含命令,可以考虑 lambda 函数。

定义 lambda 函数的形式如下:
labmda 参数:表达式 lambda 函数默认返回表达式的值。
labmda x, y=0 : x+y
会自动返回x+y
'''
def test(): 
	a = lambda x, y=1 : x+y
	print a(10)
	print (lambda x,y,z: x*y*z)(2,3,4)

'''
需要两个参数,第一个是一个处理函数,第二个是一个序列(list,tuple,dict)
map()
将序列中的元素通过处理函数处理后返回一个新的列表
filter()
将序列中的元素通过函数过滤后返回一个新的列表
reduce()
将序列中的元素通过一个二元函数处理返回一个结果
'''
def test1():
	li = [1, 2, 3, 4, 5]
	# 序列中的每个元素加1
	print map(lambda x : x+1,li)
	#[2, 3, 4, 5, 6]
	# 返回序列中的偶数,根据lambda中的条件语句进行过滤
	print filter(lambda x: x % 2 == 0, li) # [2, 4]
	#[2, 4]

	# 返回所有元素相乘的结果
	print reduce(lambda x, y: x * y, li)
	#120
	
def test2():
	'''一行代码计算任何数的阶乘
	int.__mul__整数的乘法'''
	result = (lambda k: reduce(int.__mul__, range(1,k+1),1))(3)
	print(result)

if __name__ == '__main__': 
	#test() 
	test1()
