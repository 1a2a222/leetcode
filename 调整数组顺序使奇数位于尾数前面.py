#
#
# class Solution:
#     def reOrderArray(self,alist):
#         if len(alist)<1:
#             return
#         elif len(alist)==1:
#             return alist
#
#         left = 0
#         right = len(alist)-1
#         while left<right:
#             while alist[left]
class Solution:
    # 一个类似于快排的方法, 只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变
    def reOrderArray(self, array):
        if len(array) < 1:
            return
        elif len(array) == 1:
            return array

        front = 0
        rear = len(array)-1
        while front <= rear:
            while array[front] & 0x1 == 1:
                front += 1
            while array[rear] & 0x1 == 0:
                rear -= 1
            array[front], array[rear] = array[rear], array[front]
        array[front], array[rear] = array[rear], array[front]
        return array

class Solution:
    def reOrderArray(self,array):
        even = 0
        while even<len(array):
            while even<len(array) and array[even]%2==1:
                even+=1
            odd = even+1
            while odd<len(array) and array[odd]%2==0:
                odd+=1
            if odd<len(array):
                #在这里，每次找的都是第一个偶数，它的下标每次都在往后移动一位，所以每次找的都是它
                array.insert(even,array.pop(odd))
                print(array[even+1])
                print(array)
                even+=1
            else:
                break
        return array
S = Solution()
print(S.reOrderArray([1, 2, 3,  10, 11, 12, 134, 5, 6, 7, 8, 9,]))
# print(S.ReorderOddEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# print(S.reOrderArray([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))