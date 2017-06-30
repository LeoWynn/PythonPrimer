#!/usr/bin/env python
#coding=utf-8

"""
# multi_process.py
# Created by Leo Wen on Mon Jun 26 15:13:18 CST 2017
"""

import os
import sys
import re
import multiprocessing
import time

def print_test(msg):
    for i in range(3):
        print msg
        time.sleep(1)

def test1():
    #单一进程
    p = multiprocessing.Process(target=print_test, args=('hello',))
    p.start()
    p.join()
    print 'Sub process done.'

def test2():
    #进程池，注意要用apply_async，如果落下async，就变成阻塞版本了。processes=4是最多并发进程数量。
    pool = multiprocessing.Pool(processes = 5)
    for i in range(10):
        msg = 'hello %d' % (i)
        pool.apply_async(print_test,(msg,))
    pool.close()
    pool.join()
    print 'Sub process done.'

if  __name__ == "__main__" :
    test2()
