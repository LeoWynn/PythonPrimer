#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''Module: test_yield
Created by Leo Wen on 2017-07-05 17:36:20
'''

'''
迭代器，对于string、list、dict、tuple等这类容器对象，使用for循环遍历是很方便的。在后台for语句对容器对象调用iter()函数，
iter()是python的内置函数。iter()会返回一个定义了next()方法的迭代器对象，它在容器中逐个访问容器内元素，
next()也是python的内置函数。在没有后续元素时，next()会抛出一个StopIteration异常，通知for语句循环结束。

生成器（Generator）是创建迭代器的简单而强大的工具。它们写起来就像是正规的函数，只是在需要返回数据的时候使用yield语句。
每次next()被调用时，生成器会返回它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值

生成器需要的内存空间与列表的大小无关，所以效率高于列表，降低了空间复杂度
'''

def create_generator():
    '''yield + return object'''
    for i in range(10):
        yield i*i

def test():
    '''Test'''
    print 'Please test here.'
    for i in create_generator():
        print i
    
    my_generator = create_generator() # 创建生成器对象,
    print my_generator
    for i in my_generator:
        print i
    #生成器对象只可以执行一次，运行后状态无后续元素.
    for i in my_generator:
        print "The second run:",i

class Bank(): # 让我们建个银行,生产许多ATM
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

def test1():
    hsbc = Bank()
    corner_street_atm = hsbc.create_atm()
    print(corner_street_atm.next())
    print(corner_street_atm.next())
    print([corner_street_atm.next() for cash in range(5)])
    hsbc.crisis = True
    print(corner_street_atm.next())


if __name__ == '__main__':
    test()
    test1()
