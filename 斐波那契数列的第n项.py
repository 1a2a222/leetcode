l = [0,1]
for i in range(9):
    l.append(l[-2]+l[-1])
print(l)
class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]
class Solution:
    def fibo(self,n):
        temp = [0,1]
        if n>=2:
            for i in range(2,n+1):
                temp[i%2]=temp[0]+temp[1]
        return temp[n%2]


class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            last,last_last = 1,0
            for i in range(n//2):
                last_last = last+last_last
                last = last+last_last
            return last if n%2 == 1 else last_last

if __name__ == '__main__':
    solution = Solution()
    a = solution.Fibonacci(3)
    print(a)