#!/usr/bin/env python
#coding=utf-8

"""
# sort_method.py
# Created by Leo Wen on Fri May 26 10:24:04 CST 2017
#用于记录八种常见的排序算法
"""

import os
import sys
import re

loopCount = 100000
import random
listTest =[]
for i in range(loopCount):
    listTest.append(random.randint(0,loopCount))
#修饰器，用于跟踪调用函数的时间：
import datetime
def funcTracking(func):
    callState = False
    def wrapper():
        startTime = datetime.datetime.now()
        print 'Start call %s, the time is: %s' % (func.__name__,startTime)
        func()
        finishTime = datetime.datetime.now()
        print 'goodbye %s, the time is: %s' % (func.__name__,finishTime)
        print 'The function running time: %s' % (finishTime-startTime,)
    
    return wrapper


'''
#插入排序
向已经排序的序列从后向前对比插入，遍历所有已排序的序列
算法适用于少量数据的排序，时间复杂度为O(n^2)
'''

def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            else:
                #pass
                break
            j -= 1
    return lists
@funcTracking
def test1():
    insert_sort(listTest)

'''
希尔排序
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，
对每组使用直接插入排序算法排序；随着增量逐渐减少，
每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
'''
def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group   #这是等于i
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

@funcTracking
def test2():
    print listTest
    print shell_sort(listTest)

'''
    冒泡排序
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
'''
def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

@funcTracking
def test3():
    
    print listTest
    print bubble_sort(listTest)

'''
    快速排序
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
'''
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        #当小于时跳出循环，赋值给left
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    #分成两部分进行快速排序
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
    #列表会自动改变内部值

@funcTracking
def test4():
    
    #print listTest
    quick_sort(listTest,0,len(listTest)-1)

'''
    直接排序法
    基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，
    将它与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
'''
def select_sort(lists):
    # 直接选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

@funcTracking
def test5():
    
    #print listTest
    print select_sort(listTest)

'''
    堆排序：
    堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
    可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是完全二叉树。
    大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
    在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
'''
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        #有改变时
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    #[::-1],从右到左提取，步长为1
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

@funcTracking
def test6():
    
    #print listTest
    print heap_sort(listTest)

'''
    归并排序
    归并排序是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
    将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
    
    归并过程为：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；
    否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，
    然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，
    接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。
'''
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)

@funcTracking
def test7():
    
    #print listTest
    print merge_sort(listTest)

'''
    基数排序
    基数排序（radix sort）属于“分配式排序”（distribution sort），又称“桶子法”（bucket sort）或bin sort，
    顾名思义，它是透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用，基数排序法是属于稳定性的排序，
    其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。
'''
import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

@funcTracking
def test8():
    
    #print listTest
    radix_sort(listTest,len(listTest))

#tese4:快速排序，test8:基数排序，相对比较快
#多使用快速排序法
if  __name__ == "__main__" :
	test1()


