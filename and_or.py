#!/usr/bin/env python
#coding=utf-8

"""
# and_or.py
# Created by Leo Wen on 2017年 7月 5日 星期三 18时18分30秒 CST
"""

import os
import sys
import re
import timeit

'''
在Python 中，and 和 or 执行布尔逻辑演算，返回它们实际进行比较的值之一。

and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。

引用：http://www.runoob.com/python/python-operators.html
'''

a = range(20)
def or_test():
	global a
	b = [i for i in a if 1 < i < 3 or 4 < i < 16]

def or_test1():
	global a
	b = [i for i in a if 4 < i < 16 or 1 < i < 3]
	
def and_test():
	global a
	b = [i for i in a if i % 2 == 1 and i < 3]
	
def and_test1():
	global a
	b = [i for i in a if i < 3 and i % 2 == 1]

def timeit_ctl(func):
	#pass
	#print func.__name__, " :", timeit.timeit(func, setup="from __main__ import print_hello")
	print func.__name__, " :", timeit.timeit(func)

def test():
	'''提高运行效率
	对于and，应该把满足条件少的放在前面，对于or，把满足条件多的放在前面'''
	timeit_ctl(or_test)
	timeit_ctl(or_test1)	#or 满足条件多的放在前面
	timeit_ctl(and_test)
	timeit_ctl(and_test1)	#and 满足条件少的放在前面

	'''
	or_test  : 5.48290586472
	or_test1  : 4.07509493828
	and_test  : 2.30235099792
	and_test1  : 1.32379198074
	'''


'''and-or结合用法
bool ? a : b 表达式。整个表达式从左到右进行演算，所以先进行 and 表达式的演算。 
1 and 'first' 演算值为 'first'，然后 'first' or 'second' 的演算值为 'first'。
'''
def choose(bool, a ,b):
		'''bool ? a : b'''
		return (bool and [a] or [b])
		
def test1():
		print choose(1, 2, 3)
		print choose(0, 2, 3)
		print choose(1, '', 3)
		print choose(0, '', 3)

if  __name__ == "__main__" :
	#test()
	test1()
