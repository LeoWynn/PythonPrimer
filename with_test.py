#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''
#Module: with_test
#Created by Leo Wen on 2017-06-16 09:05:28
'''

#使用类
class opened(object):
    def __init__(self,name):
        self.handle = open(name)

    def __enter__(self):
        return self.handle

    def __exit__(self,type,value,trackback):
        #3个参数，分别代表异常的类型、值、以及堆栈信息，如果没有异常，3个入参的值都为None。
        self.handle.close()

#使用上下文
from contextlib import contextmanager
'''
使用contextmanager的函数，yield只能返回一个参数，而yield后面是处理清理工作的代码。
'''
@contextmanager
def opened1(name):
    f = open(name)
    try:
        yield f
    finally:
        f.close()

def test():
    '''With Test
    with 是一种上下文管理协议用于简化try/except/finally的处理流程，
    with 通过__enter__方法初始化，__exit__方法做善后和处理异常
    
    '''
    print 'Please test here.'
    with opened1('test.txt') as f:
        print f.readlines()
    
'''
应用场景
一个确保代码执行前加锁，执行后释放锁的模板：
数据库事务的提交和回滚：
@contextmanager
    def locked(lock):
        lock.acquire()
        try:
            yield
        finally:
            lock.release()
    with locked(myLock):
        # Code here executes with myLock held.  The lock is
        # guaranteed to be released when the block is left (even
        # if via return or by an uncaught exception).
''' 


if __name__ == '__main__':
    test()
