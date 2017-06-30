#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
'''
#Module name:testtuple.py
#Created by Leo Wen  
'''
import os
import sys

'''
有序
不可重新赋值

'''

def test1():
	name = ('leo',)*10
	#name[1] = 'leo'	#tuple不允许重新赋值
	print name, len(name)
	t = (3.14, 'China', 'Jason', ['A', 'B'])
	#tuple中的list位置不可以改变，可以list的内容
	l = t[3]
	l[0] = 'leo'
	print l, len(l)







if __name__ == "__main__":test1()










