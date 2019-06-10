class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Solution:
    def reverselist(self,head):
        new_head = None
        while head!=None:
            p = head   #这里是给p赋值一个链表
            head = head.next   #这里是将头节点取走后的其余链表重新赋给head
            p.next = new_head  #这里是将p节点下面的地址的节点的值赋给新的new_head
            new_head = p       #最后重新赋值指向
        return new_head
head = None
class Solution:
    def reverse(self,head):
        new_head = None
        while head!=None:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
for count in range(1,5):
    head = Node(count,head)
head = Node(1,Node((0,None)))
head.next = None  #这里是给head.next这个变量的next赋值为空
while head!=None:
    print(head.data)
    head = head.next