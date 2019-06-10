# l1 = [[1,2,3,],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
#
# for i in l1[::2]:
#     i[::-1]
# # print(l1)
# print(l1[0][::-1])

#continue

# l = [1,1,2,2,3,4,5,6]
# for i in range(len(l)):
#     if l[i]==l[i-1] and i>0:
#         continue
#     print(i,'*'*10,l[i])

class Solution6:
    def merge(self, alist):
        if len(alist) <= 1:
            return alist
        n = len(alist)
        middle = n // 2
        left = self.merge(alist[:middle])
        right = self.merge(alist[middle:])
        l_point, r_point = 0, 0
        result = []
        while len(left) > l_point and len(right) > r_point:
            if left[l_point] < right[r_point]:
                result.append(left[l_point])
                l_point += 1
            else:
                result.append(right[r_point])
                r_point += 1
            print(result)
        result.extend(left[l_point:])
        result.extend(right[r_point:])
        return result
s = Solution6()
l = [44,2,3,5,4,2,36,9,8,7]
s.merge(l)
print(l)