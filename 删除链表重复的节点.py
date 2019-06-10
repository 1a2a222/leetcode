#这个题目有些不熟练，是需要多敲几遍的
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    """排序链表，删除链表中重复的节点，"""
    def DeleteNode(self,head):
        #在这里定义一个指针指向节点的前一位
        pre = Node(-1)
        #定义一个指针指向节点的后一位
        pre.next = head
        cur_node = head
        while head and head.next:
            if head.val==head.next.val:
                val = head.val
                #在这里开始循环，如果head存在并且val和当前值相等
                while head and val ==head.val:
                    head = head.next
                cur_node.next = head
            else:
                cur_node = head
                head = head.next
        return pre.next
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(3)
node5 = Node(4)
node6 = Node(4)
node7 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
s = Solution()
a = s.DeleteNode(node1)
while a!=None:
    print(a.val)
    a = a.next
