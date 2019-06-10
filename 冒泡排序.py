#冒泡排序是将一个序列，每次循环比较第i个和第i+1个，将大的放后面
#所以第一次是比较n-1次，第二次比较n-2次
#总共的循环次数是n-1次
def sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(n-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(0,n-j-1):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]