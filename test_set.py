#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
'''
#Module name:testset.py
#Created by Leo Wen  
'''
import os
import sys

'''
无序
不可以重复
所以如果我们要判断一个元素是否在一些不同的条件内符合，用set是最好的选择，下面例子：
python dict和set都是使用hash表来实现，查找元素的时间复杂度是O(1)，

'''

def test1():
	s = set(['A', 'B', 'C','A'])
	s.add('D')
	s.remove('A')
	print s,len(s)
	print 'A' in s

	#遍历
	s1 = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
	#tuple
	for x in s1:
 		print x[0],':',x[1]
	months = set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',])
	x1 = 'Feb'
	x2 = 'Sun'
	if x1 in months:
		print 'x1: ok'
	else:
		print 'x1: error'




if __name__ == "__main__":test1()










