#分成两个序列，一个是无序的，一个是有序的，对无序的那个进行取值，然后和前面那个有序的及逆行比较
#如果比较小，就放到前面去,然后和前面有序序列依次比较，如果取值比较的第一个就最大，那么可以直接跳出当次循环
#
def sort(alist):
    n = len(alist)
    for j in range(1,n):
        i = j
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -=1
            else:
                break
l = [3,6,3,2,1,2,3,6,5]
sort(l)
print(l)
def sort(alist):
    n =len(alist)
    for i in range(1,n):
        for j in range(i,1,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]