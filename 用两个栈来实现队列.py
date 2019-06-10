class Stack:
    """栈的实现"""
    def __init__(self):
        self.__list = []
    def push(self,node):
        self.__list.append(node)
    def pop(self):
        self.__list.pop()
    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        return self.__list == []
    def size(self):
        return len(self.__list)
class Queue:
    """队列的实现"""
    def __init__(self):
        self.__list = []
    def enqueue(self,node):
        """入队操作"""
        self.__list.append(node)
    def dequeue(self):
        self.__list.pop(0)
    def is_empty(self):
        return self.__list ==[]
    def size(self):
        return len(self.__list)

class Solution:
    """用两个栈来实现队列"""
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
    def push(self,node):
        self.__stack1.append(node)
    def pop(self):
        if len(self.__stack1)==0 and len(self.__stack2)==0:
            return
        elif len(self.__stack2)==0:
            while len(self.__stack1)>0:
                self.__stack2.append(self.__stack1.pop())
        return self.__stack2.pop()
queue = Solution()
for i in range(10):
    queue.push(i)
for i in range(10):
    a = queue.pop()
    print(a,end=' ')