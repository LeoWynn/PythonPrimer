#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''Module: if_else
Created by Leo Wen on 2017-07-06 17:47:45
'''

def test():
    '''三元操作符是 if-else 语句也就是条件操作符的一个快捷方式：'''
    print 'Please test here.'
    y = 9
    x = 10 if (y == 9) else 20
    print x
    y = 8
    x = 10 if (y == 9) else 20
    print x

def small(a, b, c):
    '''多个条件表达式链接起来用以计算最小值'''
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)

def test1():
    print small(30, 4, 5)
    
    '''列表推导中使用三元运算符'''
    a = [m**2 if m > 10 else m**4 for m in range(50)]
    print a 

if __name__ == '__main__':
    test()
    test1()
