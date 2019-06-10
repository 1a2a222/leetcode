
class Solution:
    """二叉搜索树的后序遍历"""
    def post_order(self,root):
        last = root[-1]
        n = len(root)
        for i in range(n):
            if root[i]>last:
                index = i
            break
        for j in range(i,n):
            if root[i]<last:
                return False
        while root:
            last = root[-1]
            for i in root:
                