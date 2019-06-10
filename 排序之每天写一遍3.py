class Solution:
    def bubble(self,alist):
        n = len(alist)
        for j in range(0,n-1):
            for i in range(0,n-1-j):
                if alist[i]>alist[i+1]:
                    alist[i],alist[i+1]=alist[i+1],alist[i]
class Solution1:
    def select(self,alist):
        n  = len(alist)
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
                if alist[j]<alist[min_index]:
                    min_index = j
            alist[min_index],alist[i] = alist[i],alist[min_index]
class Solution3:
    def insert(self,alist):
        n = len(alist)
        for i in range(1,n):
            for j in range(i,0,-1):
                if alist[j]<alist[j-1]:
                    alist[j],alist[j-1]=alist[j-1],alist[j]
class Solution3_co:
    def insert(self,alist):
        n = len(alist)
        for i in range(1,n):
            while i>0:
                if alist[i]<alist[i-1]:
                    alist[i],alist[i-1]=alist[i-1],alist[i]
                    i-=1
                else:
                    break
class Solution4:
    def quick(self,alist,start,end):
        if start>end:
            return
        left = start
        right = end
        middle = alist[start]
        while left<right:
            while left<right and alist[right]>=middle:
                right-=1
            alist[left] = alist[right]
            while left<right and alist[left]<middle:
                left+=1
            alist[right]=alist[left]
        alist[left]=middle
        self.quick(alist,0,left-1)
        self.quick(alist,left+1,end)
class Solution5:
    def shell(self,alist):
        n = len(alist)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                while i > 0:
                    if alist[i] < alist[i - gap]:
                        alist[i], alist[i - gap] = alist[i - gap], alist[i]
                        i -=1
                    else:
                        break
            gap //= 2

class Solution6:
    def merge(self, alist):
        if len(alist) <= 1:
            return alist
        n = len(alist)
        middle = n // 2
        left = self.merge(alist[:middle])
        right = self.merge(alist[middle:])
        l_point, r_point = 0, 0
        result = []
        while len(left) > l_point and len(right) > r_point:
            if left[l_point] < right[r_point]:
                result.append(left[l_point])
                l_point += 1
            else:
                result.append(right[r_point])
                r_point += 1
            print(result)
        result.extend(left[l_point:])
        result.extend(right[r_point:])
        return result

def wrap(func):
    def inner(*args,**kwargs):
        print('before func')
        ret = func(*args,**kwargs)
        print('after func')
        return ret
    return inner
def wrap1(func):
    def inner(*args,**kwargs):
        print('before func1')
        ret = func(*args,**kwargs)
        print('after func1')
        return ret
    return inner

s = Solution6()
l = [44,2,3,5,4,2,36,9,8,7]

s.merge(l)
print(l)
