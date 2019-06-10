
class Node:
    def __init__(self,x):
        self.root = x
        self.lchild = None
        self.rchild = None
class Solution:
    """输入两颗二叉树啊A,B，判断B是不是A的子结构"""
    def HasSubtree(self,root1,root2):
