class Node:
    def __init__(self,x):
        self.val = x
        self.lchild = None
        self.rchild = None

class Solution:
    def convert(self,root_tree):
        if root_tree is None:
            return
        if not root_tree.lchild and not root_tree.rchild:
            return root_tree
        #处理左子树
        self.convert(root_tree.lchild)
        lchild = root_tree.lchild
        #连接左子树与根的最大节点
        if lchild:
            while lchild.rchild:
                left = lchild.rchild
            root_tree.lchild,lchild.rchild = lchild,root_tree