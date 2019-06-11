

class Solution:
    """判断二维数组中有没有目标值，首先获取整个列表的长度以及列表元素的长度
    然后取第一个元素的最右上角的值开始判断，如果比目标小那么行数加1
    如果比目标大那么列数建1，当行数加到比整个列表中的行数都要大的时候
    就跳出循环，返回False；此外，可以采用一个变量，再获取每一个target的时候
    进行计数，获取目标数组中该数的个数。"""
    def Find(self,alist,target):
        if alist==[]:
            return
        rawnum = len(alist)
        colnum = len(alist[0])
        i = 0
        j = colnum -1
        count =0
        while i<rawnum and j>=0:
            if alist[i][j]<target:
                i +=1
            elif alist[i][j]>target:
                j -=1
            else:
                count+=1
                j-=1
        return count