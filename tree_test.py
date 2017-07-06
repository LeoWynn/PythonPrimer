#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''
#Module: tree_test
#Created by Leo Wen on 2017-06-07 20:39:21
'''
class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.l_child = None
        self.r_child = None

class Tree(object):
    def created_tree(self,tree,n):
        data = raw_input('->')
        self.deepth = 3
        if data == '#':
            tree.data = None
        else:
            tree.data = data
            if n > 0:
                tree.l_child = TreeNode()
                self.created_tree(tree.l_child,n-1)
                tree.r_child = TreeNode()
                self.created_tree(tree.r_child,n-1)

    def visit(self,tree):
        if tree.data is not None:
            print str(tree.data),

    ## 15 层次遍历  
    def lookup(self, root):  
        #print root.data
        stack = [root] 
        print 'stack: ', stack 
        while stack:  
            current = stack.pop(0)  
            #print 'current: ', current
            print current.data,  
            if current.l_child:  
                stack.append(current.l_child)  
            if current.r_child:  
                stack.append(current.r_child)  

    def pre_order(self, tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.l_child)
            self.pre_order(tree.r_child)

    def middle_order(self,tree):
        if tree is not None:
            self.middle_order(tree.l_child)
            self.visit(tree)
            self.middle_order(tree.r_child)
    def post_order(self,tree):
        if tree is not None:
            self.post_order(tree.l_child)
            self.post_order(tree.r_child)
            self.visit(tree)

    def init(self):
        self.sum_lists = []

    def sum_tree(self,tree,sums=0):
        if not hasattr(tree,'data'):
            self.sum_lists.append(sums)
            print self.sum_lists
        else:
            if tree.data is not None:
                sums1 = sums + int(tree.data)
                print 'sums:', sums
                self.sum_tree(tree.l_child,sums1)
                self.sum_tree(tree.r_child,sums1)
                del sums1

def test():
    '''Test '''   
    t = TreeNode()
    tree = Tree()
    tree.created_tree(t,3)
    tree.pre_order(t)
    print '\n'    
    tree.middle_order(t)
    print '\n'
    tree.post_order(t)
    print '\n'
    tree.init()
    tree.sum_tree(t)
    tree.lookup(t)

    
if __name__ == '__main__':
    test()
