class Node:
    def __init__(self,x):
        self.val = x
        self.lchild = None
        self.rchild = None
class Solution:
    """打印二叉树中节点值的和为输入整数的所有路径"""
    def Findpath(self,root,num):
        """定义一个patharray,"""
        patharray = []
        def ispath(root,num,onepath=[]):
            if num>root.val:
                onepath.append(root.val)
                if root.lchild!=None:
                    ispath(root.lchild,num-root.val,onepath)
                if root.rchild!=None:
                    ispath(root.rchild,num-root.val,onepath)
            elif num==root.val:
                onepath.append(root.val)
                if root.rchild==None and root.lchild==None:
                    tmp = onepath[:]
                    patharray.append(tmp)
            else:
                #这里这个数字是随便添加的，目的是当最后这个循环没有得到值，进入到下面的函数时，可以通过pop
                #来返回上一层
                onepath.append(5)
            onepath.pop()
        ispath(root,num)
        return patharray
pNode1 = Node(10)
pNode2 = Node(5)
pNode3 = Node(12)
pNode4 = Node(4)
pNode5 = Node(7)


pNode1.lchild = pNode2
pNode1.rchild = pNode3
pNode2.lchild = pNode4
pNode2.rchild = pNode5
s = Solution()
a = s.Findpath(pNode1,22)
print(a)