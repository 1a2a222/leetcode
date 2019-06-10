

class Node:
    def __init__(self,x):
        self.root = x
        self.lchild = None
        self.rchild = None
class Solution:
    """给一个二叉树，将其转变成镜像"""
    def Mirror(self,root):
        """递归实现"""
        if not root:
            return
        p = root.lchild
        root.lchild = root.rchild
        root.rchild = root.lchild
        self.Mirror(root.lchild)
        self.Mirror(root.rchild)
    def Mirror2(self,root):
        """新建一个队列来存储这个每次遍历的树，当这个树有值的时候，就取这个数的最后一个元素
        开始遍历，如果树的左子树不为空或者右子树不为空，就添加到队列里面，进行左右子树的更换，直到
        左右子树都为空为止"""
        stackNode = [root]
        while stackNode:
            n= len(stackNode)-1
            tree = stackNode[n]
            stackNode.pop()
            if tree.lchild !=None or tree.rchild!=None:
                tree.lchild,tree.rchild=tree.rchild,tree.lchild
            if tree.lchild:
                stackNode.append(tree.lchild)
            if tree.rchild:
                stackNode.append(tree.rchild)
