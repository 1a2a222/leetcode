
class Node:
    def __init__(self,x):
        self.val = x
        self.lchild = None
        self.rchild = None
class Solution:
    """从上到下打印二叉树，其实就是层次遍历，通过一个队列，来判断，左边一直取，右边一直添加，知道整个序列的值
    都被取完，到None为止"""
    def printfromtop2tail(self,root):
        if root is None:
            return
        queue = [root]
        while queue:
            cur_node = queue.pop(0)
            print(root.val)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
