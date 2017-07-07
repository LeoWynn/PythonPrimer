#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''Module: string_usage
Created by Leo Wen on 2017-07-07 10:34:16
'''

'''
    ASCII 编码：包含127个字符，英文字母／数字／符号
    GB2312编码：中国汉字
    Unicode把所有语言都统一到一套编码里
    UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，
    只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：
    在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
    
'''

def test():
    '''Test'''
    print 'Please test here.'
    print 'ABC'.encode('ascii')
    print str('中')

def test1():
    string_test = "python String function"
    print len(string_test)  #字符串长度
    '''
        字母处理, 并不改变字符串对象，
        全部大写：string_test.upper()
        全部小写：str.lower()
        大小写互换：str.swapcase()
        首字母大写，其余小写：str.capitalize()
        首字母大写：str.title()
    '''
    print string_test.upper()
    print string_test.lower()
    print string_test.swapcase()
    print string_test.capitalize()
    print string_test.title()
    print string_test


def test2():
    string_test = "python String function"
    '''
        格式化相关,
        获取固定长度，右对齐，左边不够用空格补齐：str.rjust(width)
        获取固定长度，左对齐，右边不够用空格补齐：str.ljust(width)
        获取固定长度，中间对齐，两边不够用空格补齐：str.center(width)
        获取固定长度，右对齐，左边不足用0补齐: str.zfill(width)
    '''
    print '%s ljust=%s' % (string_test,string_test.ljust(50))
    print '%s rjust=%s' % (string_test,string_test.rjust(50))
    print '%s center=%s' % (string_test,string_test.center(50))
    print '%s zfill=%s' % (string_test,string_test.zfill(50))
    print '%50s' % string_test  #右对齐
    print '%-50s' % string_test #左对齐

def test3():
    string_test = "python String function"
    '''
        字符串搜索相关
        搜索指定字符串，没有返回-1：str.find('t')
        指定起始位置搜索：str.find('t',start)
        指定起始及结束位置搜索：str.find('t',start,end)
        从右边开始查找：str.rfind('t')
        搜索到多少个指定字符串：str.count('t')
        上面所有方法都可用index代替，不同的是使用index查找不到会抛异常，而find返回-1
    '''
    print '%s find nono=%d' % (string_test,string_test.find('nono'))
    print '%s find t=%d' % (string_test,string_test.find('t'))
    print '%s find t from %d=%d' % (string_test,1,string_test.find('t',1))
    print '%s find t from %d to %d=%d' % (string_test,1,2,string_test.find('t',1,2))
    #print '%s index nono ' % (string_test,string_test.index('nono',1,2))
    print '%s rfind t=%d' % (string_test,string_test.rfind('t'))
    print '%s count t=%d' % (string_test,string_test.count('t'))

def test4():
    string_test = "python String function"
    '''
    字符串替换相关
    替换old为new：str.replace('old','new')
    替换指定次数的old为new：str.replace('old','new',maxReplaceTimes)
    '''
    print '%s replace t to *=%s' % (string_test,string_test.replace('t', '*'))
    print '%s replace t to *=%s' % (string_test,string_test.replace('t', '*',1))
    '''
    字符串去空格及去指定字符
    去两边空格：str.strip()
    去左空格：str.lstrip()
    去右空格：str.rstrip()
    去两边字符串：str.strip('d')，相应的也有lstrip，rstrip
    '''
    print '%s strip=%s' % (string_test,string_test.strip())
    print '%s strip=%s' % (string_test,string_test.strip('d'))
    '''
    按指定字符分割字符串为数组：str.split(' ')
    默认按空格分隔
    '''
    str='a b c de'
    print '%s strip=%s' % (str,str.split())
    str='a-b-c-de'
    print '%s strip=%s' % (str,str.split('-'))

def test5():
    '''
    字符串判断相关
    是否以start开头：str.startswith('start')
    是否以end结尾：str.endswith('end')
    是否全为字母或数字：str.isalnum()
    是否全字母：str.isalpha()
    是否全数字：str.isdigit()
    是否全小写：str.islower()
    是否全大写：str.isupper()
    '''
    str='python String function'
    print '%s startwith t=%s' % (str,str.startswith('t'))
    print '%s endwith d=%s' % (str,str.endswith('d'))
    print '%s isalnum=%s' % (str,str.isalnum())
    str='pythonStringfunction'
    print '%s isalnum=%s' % (str,str.isalnum())
    print '%s isalpha=%s' % (str,str.isalpha())
    print '%s isupper=%s' % (str,str.isupper())
    print '%s islower=%s' % (str,str.islower())
    print '%s isdigit=%s' % (str,str.isdigit())
    str='3423'
    print '%s isdigit=%s' % (str,str.isdigit())


if __name__ == '__main__':
    test5()
