

class Solution:
    """首先是新建一个字典存储每个数字的个数，然后遍历这个字典，将数字的个数大于1的字典的key添加到
    一个result列表中"""
    def Find(self,alist):
        dic = {}
        result = []
        for i in alist:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic.keys():
            if dic[i]>1:
                result.append(i)
        return result

s = Solution()
a = s.Find([2,3,1,0,2,5,3])
print(a)