
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.special = None
class Solution:
    """输入一个复杂链表，一个节点指向下一个节点，
    一个指针指向任意一个节点"""
    def Clone(self,head):
        if head==None:
            return
        self.Clone(head)
        

class Solution:
    def clone(pHead):
        if pHead == None:
            return None
        # 复制节点在原节点之后
        pCur = pHead
        while (pCur != None):
            node = Node(pCur.val)
            node.next = pCur.next
            pCur.next = node
            pCur = node.next
        # 复制random节点
        pCur = pHead
        while (pCur != None):
            if pCur.random != None:
                pCur.next.random = pCur.random.next
            pCur = pCur.next.next
        head = pHead.next
        cur = head
        # 将新旧链表分离
        pCur = pHead
        while (pCur != None):
            pCur.next = pCur.next.next
            if cur.next != None:
                cur.next = cur.next.next
            cur = cur.next
            pCur = pCur.next
        return head