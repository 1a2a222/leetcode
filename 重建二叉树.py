

class Node:
    def __init__(self,x):
        self.val =x
        self.lchild = None
        self.rchild = None
class Solution:
    def __init__(self):
        self.root = None
    def reConstructtree(self,pre,tin):
        """
        先序遍历：根左右
        中序遍历：左根右
        """
        if not pre and not tin:
            return
        root = Node(pre[0])
        #i是取中序遍历中根节点的下表
        i = tin.index(pre[0])
        root.lchild  = self.reConstructtree(pre[1:i+1],tin[:i])
        root.rchild = self.reConstructtree(pre[i+1:],tin[i+1:])#这里注意由于中序遍历的根节点在中间，所以要从i+1开始去右子树的值
        return root
    def printwidth(self,root):
        if root is None:
            return
        queue = [root]
        while queue:
            #每次取最左边的节点，当取完后，没有节点了就结束循环
            cur_node = queue.pop(0)
            print(cur_node.val,end='')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
            print(len(queue))
if __name__ == '__main__':
    solution = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    a = solution.reConstructtree(pre,tin)

    solution.printwidth(a)

    # solution.printdeepth(a)