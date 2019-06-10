

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    """这个是将链表反转，可以通过画图来看到整个遍历的步骤,这个和从头到尾打印链表不一样"""
    def reverse(self,head):
        if not head or not head.next:
            return head
        new_head = None
        while head!=None:
            p = head
            head  = head.next
            p.next = new_head
            new_head = p
        return new_head
class Solution:
    def solu(self,alists):
        new_head = None
        while alists!=None:
            p = alists
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
node1 = Node(10)
node2 = Node(11)
node3 = Node(13)
node1.next = node2
node2.next = node3
s = Solution()
p = s.reverse(node1)
while p!=None:
    print(p.data)
    p = p.next






# class Solution:
#     def reverselist(self,head):
#         new_head = None
#         while head!=None:
#             p = head   #这里是给p赋值一个链表
#             head = head.next   #这里是将头节点取走后的其余链表重新赋给head
#             p.next = new_head  #这里是将p节点下面的地址的节点的值赋给新的new_head
#             new_head = p       #最后重新赋值指向
#         return new_head
# head = None
# class Solution:
#     def reverse(self,head):
#         new_head = None
#         while head!=None:
#             p = head
#             head = head.next
#             p.next = new_head
#             new_head = p
# for count in range(1,5):
#     head = Node(count,head)
# head = Node(1,Node((0,None)))
# head.next = None  #这里是给head.next这个变量的next赋值为空
# while head!=None:
#     print(head.data)
#     head = head.next