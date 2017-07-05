#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''Module: copy_deepcopy
Created by Leo Wen on 2017-07-05 17:19:09
'''

'''
    1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
    2. copy.deepcopy 深拷贝 拷贝对象及其子对象
    3. = 赋值是传对象的引用
'''

import copy
def test():
    '''Test'''
    print 'Please test here.'
    a = [1, 2, 3, 4, ['a', 'b']]  #原始对象
    b = a #赋值，传对象的引用
    c = copy.copy(a)  #对象拷贝，浅拷贝,
    d = copy.deepcopy(a)  #对象拷贝，深拷贝,
    a.append(5)  #修改对象a
    a[4].append('c')  #修改对象a中的['a', 'b']数组对象
    print a
    print b
    print c
    print d
    
    '''
    [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    [1, 2, 3, 4, ['a', 'b', 'c']]
    [1, 2, 3, 4, ['a', 'b']]
    '''



if __name__ == '__main__':
    test()
