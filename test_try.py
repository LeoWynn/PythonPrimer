#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
'''
#Module name:testTry.py
#Created by Leo Wen  
'''
import os
import sys

#捕获所有异常，使用Exception,e
def test1():
	try:
		a = 10 
		del(a)
		b = a
	except Exception,e:
		print Exception,':',e

#使用traceback模块，跟踪执行中的异常，print_exc()
import traceback
def test2():
	try:
		a = 10 
		del(a)
		b = a
	except:
		traceback.print_exc()

#利用sys模块回溯最后的异常
def test3():
	try:
		a = 10 
		del(a)
		b = a
	except:
		info = sys.exc_info()
		print info[0],':',info[1]
		f = open('./log.txt','a')
		f.write('%s:%s\n' % (info[0],info[1]))
		f.flush()
		f.close()

#把异常存入到log中
import traceback
def test4():
	try:
		a = 10 
		del(a)
		b = a
	except:
		#info = traceback.print_exc()
		#print info
		f = open('./log.txt','a')
		traceback.print_exc(file=f)
		#for i in info:
		#f.write('%s' % info)
		f.flush()
		f.close()
#测试读
def test5():
	f = open('./log.txt','r')
	#print 'read:',f.read()	#读取全文
	print 'readline:',f.readline()	#读一行
	print f.tell()	#一行的字符数

	print 'readlines:',f.readlines()
	print f.tell()



if __name__ == "__main__":test5()










