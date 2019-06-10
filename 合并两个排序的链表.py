

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    """合并两个有序链表，让他们合并后依然具有顺序"""
    def Merge(self,head1,head2):
        if head1==None:
            return head2
        if head2 == None:
            return head1
        new_head = None
        if head1.val<head2.val:
            new_head = head1
            new_head.next = self.Merge(head1.next,head2)
        else:
            new_head  = head2
            new_head.next = self.Merge(head1,head2.next)
        return new_head
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6
s = Solution()
p = s.Merge(node4,node1)
while p!=None:
    print(p.val)
    p = p.next