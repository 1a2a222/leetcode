#选择排序是将两个排序的index的最小值给记住，从无序的序列中去找，找到最小的
#往前面去放，也就是去找最小值

def sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1,n-1):
            if alist[j]>alist[i]:
                min = i
        alist[j],alist[i]=alist[i],alist[j]
def select_sort(alist):
    n = len(alist)
    for j in range(0,n-1):
        min_index = j
        for i in range(j+1,n):
            if alist[min_index]>alist[i]:
                min_index = i
        alist[min_index],alist[j] = alist[j],alist[min_index]
li = [2,1,2,3,5,3,2,1,2,5,3,2]
select_sort(li)
print(li)

def select(alist):

    n = len(alist)
    for j in range(0,n-1):
        min = j
        for i in range(j+1,n):
            if alist[j]>alist[i]:
                min = i
        alist[j],alist[i] = alist[i],alist[j]