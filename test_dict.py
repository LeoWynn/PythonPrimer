#!/usr/bin/env python
#-*- coding: UTF-8 -*-
 
'''
#Module name:testdict.py
#Created by Leo Wen  
'''
import os
import sys

'''
无序
可通过key重新赋值,key是不可以变的，可以用tuple当key,用list当values
key不可用重复

可以直接通过键值对方式添加dict中的元素
查找速度快。无论是10个还是10万个，速度都是一样的，但是代价是耗费的内存大。
List相反，占用内存小，但是查找速度慢。
'''


def test1():
	d = {
		'Adam': 95,
		'Lisa': 85,
		'Bart': 59,
		'Paul': 75
	}
	d['Adam'] = 100
	d['Leo'] = 95	#可用通过键值对直接添加dict元素
	print d,len(d)
	#如需要访问最好先判断是否存在，防止报错
	if 'Adam' in d : print 'exist key'

	print d.get('Leo')	#使用get可以直接查看，无时返回None

	#遍历时是遍历dict中的所有key
	for key in d:
		print key,':',d.get(key)

	d1 = {'jone':22, 'ivy':17}
	#利用dict的items()属性进行dict的合并
	#d2 = dict(d.items() + d1.items())
	#d2 = dict(d,**d1)
	#方法2和方法3速度很快，效果一样
	d2 = dict(d)
	d2.update(d1)
	print d2,'d2 len:',len(d2)

	name = d2.keys()	#返回list
	value = d2.values()
	print name,len(name)
	print value,len(value)
	
	#使用zip组合两个list，转化成字典
	d3 = dict(zip(name,value))
	print d3








if __name__ == "__main__":test1()










