

class Solution:
    def replaceSpace(self,s):
        len_space = 0
        for i in s:
            if i==' ':
                len_space+=1
        newstr = [None]*(len(s)+len_space*2)
        index_old = 0
        index_new = 0
        while index_new<len(newstr) and index_old<len(s):
            if s[index_old]==' ':
                newstr[index_new:index_new+3]=['%','2','0']
                index_new+=3
                index_old+=1
            else:
                newstr[index_new]=s[index_old]
                index_new+=1
                index_old+=1
        return "".join(newstr)

s = Solution()
a = s.replaceSpace('fdas fdasjlkjl fdjlkji')
print(a)