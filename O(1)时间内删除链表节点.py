class Node:
    def __init__(self,x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    """这是删除链表中的一个已知节点，不是重复的节点，用到的方法是取当前要删除节点的
    下一个节点，将下一个节点的值赋给这个要删除的节点，然后把下一个节点的指向也赋给这个
    要删除的节点，最后删除下一个节点"""
    def DeleteNode(self,pHead,delete_node):
        if not pHead or not delete_node:
            return
        if delete_node.next!=None:
            pNext = delete_node.next
            delete_node.val = pNext.val
            delete_node.next = pNext.next
            pNext.__del__()
        elif delete_node==pHead:
            pHead.__del__()
            delete_node.__del__()
        else:
            pNode = pHead
            while pHead!=delete_node:
                pHead = pHead.next
            pHead.next = None
            delete_node.__del__()