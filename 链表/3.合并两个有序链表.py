class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists( l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None and l2 == None:
        return None
    l = ListNode(0)
    pre = l
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            pre.next = l1
            l1 = l1.next   #也就是说在这一步一直在改变l1的值
        elif l1.val > l2.val:
            pre.next = l2
            l2 = l2.next  #同理，在这一步一直在改变l2的值
        pre = pre.next
    if l1 is None:
        pre.next = l2
    if l2 is None:
        pre.next = l1
    return l.next

head = ListNode(1)
m1 = ListNode(2)
head.next = m1
# head2 = ListNode(1)
m2 = ListNode(3)
a = head
a.next=m2
# head2.next = m2
# a = mergeTwoLists(head,head2)
# print(a)
while head:
    print(head.val,end=" ")
    head = head.next

# def quick_sort(array):
#     index = 0
#     pivot = array[0]
#     left = [i for i in array[index+1] if i <= pivot]
#     right = [i for i in array[index+1] if i>pivot]
#     return quick_sort(left)+pivot+quick_sort(right)