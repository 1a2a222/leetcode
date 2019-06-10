class Solution:
    def shell(self,alist):
        n =len(alist)
        gap = n//2
        while gap>0:
            for j in range(gap,n):
                i=j
                while i>0:
                    if alist[i]<alist[i-gap]:
                        alist[i],alist[i-gap]=alist[i-gap],alist[i]
                        i-=1
                    else:
                        break
            gap//=2
if __name__ == '__main__':
    soul = Solution()
    l = [5,3,2,1,4,7,8,5,23,6,9,8]
    soul.shell(l)
    print(l)