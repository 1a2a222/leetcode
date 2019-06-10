
class Solution:
    def bubble(self,alist):
        n = len(alist)
        for j in range(0,n-1):
            for i in range(0,n-1-j):
                if alist[i]>alist[i+1]:
                    alist[i],alist[i+1]= alist[i+1],alist[i]
class Solution2:
    def select(self,alist):
        n = len(alist)
        for j in range(n-1):
            min_index = j
            for i in range(j+1,n):
                if alist[i]<alist[min_index]:
                    min_index = i
            alist[min_index],alist[j] = alist[j],alist[min_index]
class Solution3:
    def insert(self,alist):
        n = len(alist)
        for i in range(n):
            for j in range(i,0,-1):
                if alist[j]<alist[j-1]:
                    alist[j],alist[j-1]=alist[j-1],alist[j]
                else:
                    break
class Solution3_co:
    def insert(self,alist):
        n = len(alist)
        for i in range(n):
            while i>0:
                if alist[i]<alist[i-1]:
                    alist[i],alist[i-1]= alist[i-1],alist[i]
                    i-=1
                else:
                    break
class Solution4:
    def shell(self,alist):
        n = len(alist)
        gap = n//2
        while gap > 0:
            for i in range(gap,n):
                while i>0:
                    if alist[i]<alist[i-gap]:
                        alist[i],alist[i-gap]=alist[i-gap],alist[i]
                        i-=1
                    else:
                        break
            gap//=2
class Solution5:
    def quick(self,alist,start,end):
        if start>end:
            return
        left = start
        right = end
        #这里得直接记下索引的值，不能记下索引，因为索引的值每回合都有可能在变
        middle_index = alist[start]
        while left<right:
            while left<right and alist[right]>=middle_index:
                right-=1
            alist[left]=alist[right]
            while left<right and alist[left]<middle_index:
                left+=1
            alist[right]=alist[left]
        alist[left]=middle_index
        self.quick(alist,0,left-1)
        self.quick(alist,left+1,end)
class Solution6:
    def merge(self,alist):
        if len(alist) <= 1:
            return alist
        n = len(alist)
        middle = n // 2
        left = self.merge(alist[:middle])
        right = self.merge(alist[middle:])
        # print(left,right)
        lp,rp = 0,0
        result = []
        while lp<len(left) and rp<len(right):
            if left[lp]<right[rp]:
                result.append(left[lp])
                lp+=1
            else:
                result.append(right[rp])
                rp+=1
        result.extend(left[lp:])
        result.extend(right[rp:])
        #这里必须要有一个返回值，和之前的右边的列表进行对比
        return result
        # l_point, r_point = 0, 0
        # result = []
        # while len(left) > l_point and len(right) > r_point:
        #     if left[l_point] < right[r_point]:
        #         result.append(left[l_point])
        #         l_point += 1
        #     else:
        #         result.append(right[r_point])
        #         r_point += 1
        #     print(result)
        # result.extend(left[l_point:])
        # result.extend(right[r_point:])


s = Solution6()
l = [44,2,3,5,4,2,36,9,8,7]
s.merge(l)
print(l)