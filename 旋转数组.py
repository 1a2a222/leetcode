class Search:
    def search(self,array,item):
        n = len(array)
        left = 0
        right = n-1
        while left<=right:
            min = (left+right) // 2
            if array[min]==item:
                return array[min],min
            elif array[min]<item:
                left =min+1
            else:
                right=min-1
        return


class Solution:
    """旋转数组的最小值，也就是排序，和快排一样,这个是错误的，不是考虑怎么排序，
    而是考虑二分查找的变形"""
    def minNumberinrotatearrat(self,array,start,end):
        if len(array)==0:
            return 0
        if start>end:
            return
        left = start
        right = end
        middle = array[start]
        while left<right:
            while array[right]>=middle and left<right:
                right -=1
            array[left] = array[right]
            while array[left]<middle and left<right:
                left+=1
            array[right] = array[left]
        array[left]=middle
        self.minNumberinrotatearrat(array,start,left-1)
        self.minNumberinrotatearrat(array,left+1,end)

class Solution2:
    def minnuminaarrty(self,array):
        """这个是有用的,针对这个题目"""
        n = len(array)
        left  = 0
        right = n-1
        minval = array[0]
        if array[left]<array[right]:
            return array[0]
        else:
            while (right-left)>1:
                mid = (left+right)//2  #注意，在这里不能使用n（列表的长度）来取中间值，因为，这个值每时每刻都是在变的
                if array[mid]>array[left]:
                    left = mid
                elif array[mid]<array[right]:
                    right = mid
                else:
                    if array[mid]==array[left] and array[left]==array[right]:
                        for i in range(1,n):
                            if array[i]<minval:
                                minval = array[i]
                                right = i
            minval = array[right]
        return minval


if __name__ == '__main__':
    solu = Solution2()
    l = [999,8888,66666,6,8,9,66,88,99,]
    a = solu.minnuminaarrty(l)
    print(a)
    ser = Search()
    l2 = [3,4,5,6,7,8,9]
    a,b = ser.search(l2,6)
    print(a,b)
