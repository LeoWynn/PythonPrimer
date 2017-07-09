#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''Module: reverse_usage
Created by Leo Wen on 2017-07-06 21:44:23
四种翻转字符串/列表的方式
'''


def test():
    '''Test'''
    print 'Please test here.'
    # 翻转列表本身
    testList = [1, 3, 5]
    testList.reverse()  #对象的方法改变列表对象本身
    print(testList)
    
    #在一个循环中翻转并迭代输出
    for element in reversed([1,3,5]):
        print(element)

    #使用切片翻转列表
    print [1, 3, 5][::-1]

    #一行代码翻转字符串
    print "Test Python"[::-1]


if __name__ == '__main__':
    test()
