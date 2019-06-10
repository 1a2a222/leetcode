# #二分查找
# #https://baike.baidu.com/item/%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE/10628618?fr=aladdi
# # n
# def bin_search(data_list, val):
#     low = 0                         # 最小数下标
#     high = len(data_list) - 1       # 最大数下标
#     while low <= high:
#         mid = (low + high) // 2     # 中间数下标
#         if data_list[mid] == val:   # 如果中间数下标等于val, 返回
#             return mid
#         elif data_list[mid] > val:  # 如果val在中间数左边, 移动high下标
#             high = mid - 1
#         else:                       # 如果val在中间数右边, 移动low下标
#             low = mid + 1
#     return # val不存在, 返回None
# ret = bin_search(list(range(1, 10)), 3)
# print(ret)
# #冒泡排序
# def bubble_sort(list):
#     count = len(list)
#     for i in range(0,count):
#         for j in range(i+1,count):
#             if list[i]<list[j]:
#                 list[j+1],list[j]=list[j],list[j+1]
#     return list
# print(bubble_sort([9,6,5,4,8]))
# #插入排序
# #https://www.cnblogs.com/AlwinXu/p/5444799.html
# def sort(list_):
#     count = len(list_)
#     for i in range(1,count):
#         j = i-1
#         if list_[i]<list_[j]:
#             temp = list_[i]
#             list_[i]=list_[j]
#             j = j-1
#             while list_[j]>temp and j>=0:
#                 list_[j+1]=list_[j]
#                 j = j-1
#             list_[j+1] = temp
#     return list_
# def srot(lis):
#     count=len(lis)
#     for i in range(1,count):
#         j = i-1
#         print('i:',i)
#         if lis[i]<lis[j]:
#             temp = lis[i]
#             lis[i]=lis[j]
#             j = j-1
#             while j>=0 and lis[j]>temp:
#                 lis[j+1]=lis[j]
#                 j=j-1
#             lis[j+1]=temp
#     return lis
# print(sort([5,4,3,5,3,5]))
#
# #快速排序
# #https://www.cnblogs.com/AlwinXu/p/5424905.html
def quick_sort(list,left,right):
    if left<right:
        i,j = left,right
        base = list[i]
        while i<j:
            while (i<j)and (list[j]>=base):
                j = j-1
            list[i]=list[j]
            while i<j and list[i]<=base:
                i=i+1
            list[j]=list[i]
        list[i]=base
        quick_sort(list,left,i-1)
        quick_sort(list,j+1,right)
    return list

print(quick_sort([9,6,5,6,5,4,6],0,6))
#
#
#
print(110)
# def quick_s(list,left,right):
#     if left<right:
#
#         i,j = left,right
#         base = list[i]
#         while i<j:
#             while list[j]>=base and i<j:
#                 j-=1
#             list[i]=list[j]
#             while list[i]<=base and i<j:
#                 i+=1
#             list[j]=list[i]
#         base = list[i]
#     quick_s(list,left,i-1)
#     quick_s(list,j+1,right)
#     return list
# print(220)
# print(quick_s([9,6,5,6,5,4,6],0,6))
# #选择排序
#https://www.cnblogs.com/AlwinXu/p/5424510.html
def select(list):
    length = len(list)
    for i in range(0,length-1):
        for j in range(i+1,length):
            if list[j]<list[i]:
                list[j],list[i]=list[i],list[j]
    return list
print(select([6,59,63,62]))
#
# #归并排序
print(9//2)
#https://www.cnblogs.com/Lin-Yi/p/7309143.html
def merge_sort(list):
    count = len(list)
    if len(list) ==1:
        return list
    mid = count//2
    left = list[:mid]
    right = list[mid:]
    l1 = merge_sort(left)
    r1 = merge_sort(right)
    return merge(l1,r1)
def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result
print(merge_sort([5,6,3]))
#
#
#
# #这里接收两个列表
# #希尔排序
#
#
#
#
