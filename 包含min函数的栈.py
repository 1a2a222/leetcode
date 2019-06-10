

class Solution:
    """定义一个栈的数据结果，在该类型中实现一个能够得到栈最小元素的min函数
    调用min，push，pop的时间复杂度都是O(1),这个题目完全根据书上的方法，可以容易实现"""
    def __init__(self):
        self.stack = []
        self.minstack = []
    def min(self):
        return self.minstack[-1]
    def push(self,node):
        self.stack.append(node)
        if self.minstack==[] or node<self.min():
            self.minstack.append(node)
        else:
            temp = self.min()
            self.minstack.append(temp)
    def pop(self):
        if self.stack==[] or self.minstack==[]:
            return
        self.minstack.pop()
        self.stack.pop()