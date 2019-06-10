

class Solution:
    def printfromtop2tail(self,root):
        queue = [root]
        result = []
        if root ==None:
            return
        while queue:
            #新建一个列表，这个列表每次循环都返回每一层的值
            row = []
            for i in queue:
                row.append(i.val)
            result.append(row)
            for i in range(len(queue)):
                cur_node = queue.pop(0)
                if cur_node.lchild is not None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)
        for i in result[1::2]:
            i = i[::-1]

        return result
