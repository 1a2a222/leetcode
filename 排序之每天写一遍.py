class Solution:
    def Bubble(self,alist):
        n = len(alist)
        for j in range(0,n-1):
            for i in range(0,n-j-1):
                if alist[i]>alist[i+1]:
                    alist[i],alist[i+1]=alist[i+1],alist[i]
class Solution2:
    def Select(self,alist):
        n = len(alist)
        for j in range(0,n-1):
            min = j
            for i in range(j+1,n):
                if alist[min]>alist[i]:
                    min = i
            alist[j],alist[min]=alist[min],alist[j]
            print('n')
class Solution3:
    def Insert(self,alist):
        n= len(alist)
        for i in range(1,n):
            for j in range(i,0,-1):
                if alist[j]<alist[j-1]:
                    alist[j],alist[j-1]=alist[j-1],alist[j]
class Solution3_2:
    def Insert_2(self,alist):
        n=len(alist)
        for j in range(1,n):
            i = j
            while i>0:
                if alist[i]<alist[i-1]:
                    alist[i],alist[i-1]=alist[i-1],alist[i]
                    i-=1
                else:
                    break
            print(alist)
class Solution4:
    def shell(self,alist):
        n = len(alist)
        gap = n//2
        while gap>0:
            for j in range(gap,n):
                i = j
                while i>0:
                    if alist[i]<alist[i-gap]:
                        alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    else:
                        break
            gap//=2
class Solution5:
    def quick(self,alist,first,last):
        if first>last:
            return
        min_value = alist[first]
        n = len(alist)
        min = first
        high = last
        while min<high:
            while min<high and alist[high]>=min_value:
                high-=1
            alist[min]=alist[high]

            while min<high and alist[min]<min_value:
                min+=1
            alist[high]=alist[min]
        alist[min]=min_value
        self.quick(alist,first,min-1)
        self.quick(alist,min+1,last)
class Solution_copy:
    def quick(self,alist,first,end):
        if first>=end:
            return
        min_value = alist[first]
        min = first
        high = end
        while min<high:
            while min<high and alist[high]>min_value:
                high-=1
            alist[min]=alist[high]
            while min<high and alist[min]<min_value:
                min-=1
            alist[high]=alist[min]
            alist[min]=min_value
        self.quick(alist,first,min-1)
        self.quick(alist,end,min+1)
class Quick:
    def quick(self,alist,start,end):
        if start>=end:
            return
        min = start
        high = end
        mid_value = alist[start]
        while min<high:
            while min<high and alist[high]>=mid_value:
                high-=1
            alist[min]=alist[high]
            while min<high and alist[min]<mid_value:
                min+=1
            alist[high]=alist[min]
        alist[min]=mid_value
        self.quick(alist,start,min-1)
        self.quick(alist,min+1,end)
        return alist
class Merge:
    def merge(self,left,right):
        l_point,r_point = 0,0
        result = []
        while l_point<len(left) and r_point<len(right):
            if left[l_point]<right[r_point]:
                result.append(left[r_point])
                l_point+=1
            else:
                result.append(right[r_point])
                r_point+=1
        result.append(left[l_point:])
        result.append(result[r_point:])
        return result
    def merge_sort(self,alist):

        n = len(alist)
        if n<=1:
            return alist
        min = n//2
        left = self.merge_sort(alist[:min])
        right = self.merge_sort(alist[min:])
        return self.merge(left,right)

if __name__ == '__main__':
    # select = Solution5()
    l = [5,3,2,1,4,7,8,5,23,6,9,8]
    # select.quick(l,0,len(l)-1)
    # print(l)
    # guibing = Quick()
    # guibing.quick(l,0,len(l)-1)
    # print(l)
    merge = Merge()
    a = merge.merge_sort(l)
    print(a)