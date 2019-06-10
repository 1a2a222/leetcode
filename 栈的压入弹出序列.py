

class Solution:
    """通过对辅助栈的压入，每次都判断是否在序列中有弹出，最后能弹完就返回True,否则就返回False"""
    def push_pop(self,list1,list2):
        stack = []
        while list2:
            if stack[-1]==list2[0] and stack:
                stack.pop()
                list2.pop(0)
            elif list2:
                stack.append(list1.pop(0))
            else:
                return False
        return True
