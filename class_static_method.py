#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''Module: class_static_method
Created by Leo Wen on 2017-07-10 21:38:26
'''
class A(object):
    '''Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,'''

    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x


def test():
    '''Test'''
    print 'Please test here.'
    a = A()
    #A.foo('hello')        #method foo() must be called with A instance as first argument
    #实例方法必须先创建实例，类不可以直接调用，类方法和静态方法都可以被实例和类调用
    a.foo('hello')
    a.class_foo('hello')
    a.static_foo('hello')
    A.class_foo('hello')
    A.static_foo('hello')
    '''
    executing foo(<__main__.A object at 0x7f282b28fdd0>,hello)
    executing class_foo(<class '__main__.A'>,hello)
    executing static_foo(hello)
    executing class_foo(<class '__main__.A'>,hello)
    executing static_foo(hello)
    '''


if __name__ == '__main__':
    test()
