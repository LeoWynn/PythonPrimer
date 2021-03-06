#!/usr/bin/env python
#coding=utf-8

"""
# sys_os.py
# Created by Leo Wen on Mon Jun 26 17:20:14 CST 2017
"""

import os
import sys


'''
    os提供一种方便的使用操作系统函数的方法。
    os.remove()删除文件
    os.rename()重命名文件
    os.walk()生成目录树下的所有文件名
    os.chdir()改变目录
    os.mkdir/makedirs创建目录/多层目录
    os.rmdir/removedirs删除目录/多层目录
    os.listdir()列出指定目录的文件
    os.getcwd()取得当前工作目录
    os.chmod()改变目录权限
    os.path.basename()去掉目录路径，返回文件名
    os.path.dirname()去掉文件名，返回目录路径
    os.path.join()将分离的各部分组合成一个路径名
    os.path.split()返回（dirname(),basename())元组
    os.path.splitext()(返回filename,extension)元组
    os.path.getatime\ctime\mtime分别返回最近访问、创建、修改时间
    os.path.getsize()返回文件大小
    os.path.exists()是否存在
    os.path.isabs()是否为绝对路径
    os.path.isdir()是否为目录
    os.path.isfile()是否为文件
'''
def test1():
    print [item for item in os.walk('./')]

'''
   sys提供访问由解释器使用或维护的变量和在与解释器交互使用到的函数
   sys.argv           命令行参数List，第一个元素是程序本身路径
   sys.modules.keys() 返回所有已经导入的模块列表
   sys.exc_info()     获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
   sys.exit(n)        退出程序，正常退出时exit(0)
   sys.hexversion     获取Python解释程序的版本值，16进制格式如：0x020403F0
   sys.version        获取Python解释程序的版本信息
   sys.maxint         最大的Int值
   sys.maxunicode     最大的Unicode值
   sys.modules        返回系统导入的模块字段，key是模块名，value是模块
   sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
   sys.platform       返回操作系统平台名称
   sys.stdout         标准输出
   sys.stdin          标准输入
   sys.stderr         错误输出
   sys.exc_clear()    用来清除当前线程所出现的当前的或最近的错误信息
   sys.exec_prefix    返回平台独立的python文件安装的位置
   sys.byteorder      本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
   sys.copyright      记录python版权相关的东西
   sys.api_version    解释器的C的API版本
   sys.version_info
'''

def test2():
    print sys.argv
    #['./sys_os.py', '1'], 返回list参数列表
    print sys.modules.keys()
    print sys.path
    print sys.version
    print sys.maxint
    print sys.maxunicode
    print sys.exec_prefix
    print copyright
    print sys.api_version
    print sys.version_info

if __name__ == "__main__":
	test2()

