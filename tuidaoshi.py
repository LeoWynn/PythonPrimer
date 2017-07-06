#!/usr/bin/env python
#coding=utf-8

"""
# tuidaoshi.py
# Created by Leo Wen on Sat May 20 10:48:45 CST 2017
"""

import os
import sys
import re


#列表推导式
def test_list():
    name_upper = []
    names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
    name_upper = [item for item in names if len(item)>3]
    print name_upper
    #
    print  [(x,y) for x in range(5) if x%2==0 for y in range(5) if y %2==1]

#嵌套列表推到式
def test_list2():
    names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],
             ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
             #包含2个e以上的名字
    d = [item for lst in names for item in lst if item.count('e') == 2 ]
    print d

#字典推导式
def test_dict():
    strings = ['import','is','with','if','file','exception']
    #字典推导式需要两个列表
    D = {key: val for val,key in enumerate(strings)}
    print D


def test_set():
    strings = ['import','is','with','if','file','exception']
    D = {item for item in strings if len(item) > 2}
    print D


if  __name__ == "__main__" :test_list2()
