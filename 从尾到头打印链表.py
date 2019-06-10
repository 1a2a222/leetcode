

class Node:
    def __init__(self,x=None):
        self.val = x
        self.next = None

class Solution:
    def printfromto(self,alist):
        if alist.val == None:
            return
        head = alist
        l = []
        while head:
            l.insert(0,head.val)
            head = head.next
        return l
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    solution = Solution()
    a = solution.printfromto(node1)
    print(a)