#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
'''
#Module name:testlist.py
#Created by Leo Wen  
'''
import os
import sys

#list的常用用法
'''
有序
可以重新赋值
可以倒序访问
也没有pop和insert、append方法。
'''

def test1():
	#空的list,
	name = [None]*10
	name[0] = 'leo'
	name.append('wen')	#扩展最后
	name.insert(1,'lijiao')	#插入扩展，增加一个元素
	print name,len(name)
	name.pop()	#删除最后一个元素
	print name,len(name)
	name.pop(2)
	print name,len(name)
def test2():
	'''	
	找到列表中出现最频繁的数
	max(...)
	max(iterable[, key=func]) -> value
	max(a, b, c, ...[, key=func]) -> value
	'''
	test = [1,2,3,4,2,2,3,1,4,4,4]
	print test.count(1)
	print(max(set(test), key=test.count))


if __name__ == "__main__":
	test1()

