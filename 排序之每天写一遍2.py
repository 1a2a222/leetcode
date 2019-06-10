class Solution:
    def bubble(self,alist):
        n = len(alist)
        for j in range(0,n-1):
            for i in range(0,n-1-j):
                if alist[i]>alist[i+1]:
                    alist[i],alist[i+1] = alist[i+1],alist[i]
class Solution1:
    def select(self,alist):
        n = len(alist)
        for j in range(0,n-1):
            min = j
            for i in range(j+1,n):
                if alist[i]<alist[min]:
                    min = i
            alist[min],alist[j] = alist[j],alist[min]
class Solution2:
    def insert(self,alist):
        n = len(alist)
        for i in range(1,n):
            while i>0:
                if alist[i]<alist[i-1]:
                    alist[i],alist[i-1]=alist[i-1],alist[i]
                    i-=1
                else:
                    break
class Solution2_co:
    def insert(self,alist):
        n = len(alist)
        for i in range(1,n-1):
            for j in range(i,0,-1):
                if alist[j]<alist[j-1]:
                    alist[j],alist[j-1]= alist[j-1],alist[j]
class Solution3:
    def quick(self,alist,start,end):
        if start>end:
            return
        n  = len(alist)
        min = alist[start]
        left = start
        high = end
        while left<high:
            while alist[high]>=min and left<high:
                high-=1
            alist[left] = alist[high]
            while alist[left]<min and left<high:
                left+=1
            alist[high]=alist[left]
        alist[left] = min
        self.quick(alist,start,left-1)
        self.quick(alist,left+1,end)
class Solution4:
    def shell(self,alist):
        n = len(alist)
        gap = n // 2
        while gap>0:
            for i in range(gap,n):
                while i>0:
                    if alist[i]<alist[i-gap]:
                        alist[i],alist[i-gap] = alist[i-gap],alist[i]
                        i-=gap
                    else:
                        break
            gap //=2


class Solution5:
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
        result.extend(left[l_point:])
        result.extend(right[r_point:])
        return result


if __name__ == '__main__':
    solution = Solution5()
    l1 = [9,6,2,4,9,6,23,26,55,3,85]
    a = solution.merge(l1)
    print(a)
