
class Solution:
    def Permutation(self,ss):
        if not len(ss):
            return []
        if len(ss)==1:
            return list(ss)
        charlist = list(ss)
        charlist.sort()
        pstr = []
        for i in range(len(charlist)):
            if i>0 and charlist[i-1]==charlist[i]:
                continue
            temp = self.Permutation(''.join(charlist[:i])+''.join(charlist[i+1:]))
            for j in temp:
                pstr.append(charlist[i]+j)
        return pstr
class Solution:
    def permination(self,ss):

class Solution1:
    def group(self,ss):
        if not len(ss):
            return []
        if len(ss)==1:
            return list(ss)
        charlist = list(ss)
        charlist.sort()
        pstr = []
        for i in range(len(charlist)):
            pstr.append(charlist[i])
            print('pstr:',pstr)
            if i>0 and charlist[i-1]==charlist[i]:
                continue
            temp = self.group(''.join(charlist[i+1:]))
            print('temp',temp)
            for j in temp:
                print('temp2:',temp)
                pstr.append(charlist[i]+j)
            pstr = list(set(pstr))
            pstr.sort()
        return pstr
s = Solution1()
a = s.group('abc')
print(a)