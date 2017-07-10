#!/usr/bin/env python 
#-*- coding: UTF-8 -*- 


''' 
#Module: typeConversion
#Created by Leo Wen on 2017-06-03 16:04:08
''' 
import os 
import sys 
import datetime 
import re 


class typeConversion(object): 
	def __init__(self): 
		pass 

'''
常见类型转换，type conversion

int(x [,base])	将x转换为一个整数
long(x [,base] )	将x转换为一个长整数
float(x)	将x转换到一个浮点数
complex(real [,imag])	创建一个复数
str(x)	将对象 x 转换为字符串
repr(x)	将对象 x 转换为表达式字符串
eval(str)	用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)	将序列 s 转换为一个元组
list(s)	将序列 s 转换为一个列表
set(s)	转换为可变集合
dict(d)	创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)	转换为不可变集合
chr(x)	将一个整数转换为一个字符
unichr(x)	将一个整数转换为Unicode字符
ord(x)	将一个字符转换为它的整数值
hex(x)	将一个整数转换为一个十六进制字符串
oct(x)	将一个整数转换为一个八进制字符串
'''

def test(): 
	name = 'hello'
	print list(name)
	print str(name)
	print tuple(name)
	print set(name)
	

if __name__ == '__main__': 
	test() 
