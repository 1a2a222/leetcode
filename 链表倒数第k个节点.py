class Node:
    def __init__(self,x=None):
        self.val = x
        self.next = None

class Solution:
    def reverse_k(self,array,k):
        if not array or k<=0:
            return
        p1 = array
        p2 = None
        for i in range(k-1):
            if p1.next!=None:
                p1 = p1.next
            else:
                return None
        p2 = array
        while p1.next!=None:
            p1 =p1.next
            p2 = p2.next
        return p2