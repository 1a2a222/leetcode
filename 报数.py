# class Solution:
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         if not n : return False
#         if n < 1:return False
#         if n == 1: return '1'
#         if n == 2: return '11'
#
#         start = '11'
#         for i in range(3,n+1):  #从第3次开始循环至数字n-1结束
#             tmp = ''
#             index = 0
#             for i in range(len(start)-1):   #循环到 start字符串长度减一结束，防止下标溢出
#                 if start[i] == start[i+1]:
#                     index += 1
#                 else:
#                     index +=1
#                     tmp += str(index)+start[i]  #str(index) ==1 ，start[i] 当前数值
#                     index = 0                 #index 归零
#
#             index +=1
#             tmp += str(index) + start[i+1]  #根据前面的index来判断最后一位是否和前一位相等，相等就加index+1，不等就是0+1，然后加上上一次循环字符串的最后一位
#             start = tmp          #内循环结束后，为下次循环的start赋值
#         return tmp
#
# a = Solution().countAndSay(6)
# print(a)
1
11
21
1211
111221
def alist(list):
    num=1
    li=[]
    i=0
    while i<len(list):
        if i!=len(list)-1:
            if list[i]==list[i+1]:
                num=num+1
            else:
                dic={}
                dic[str(list[i])] = num
                li.append(dic)
                num=1
            i=i+1
        else:
            if list[i]==list[i-1]:
                dic = {}
                dic[str(list[i])] = num
                li.append(dic)
            else:
                dic = {}
                dic[str(list[i])] = 1
                li.append(dic)
            i=i+1
    lis=[]
    print(li)
    return lis

result=[1]
for i in range(0,3):
    result=alist(result)
print(result)