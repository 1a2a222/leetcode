#
#
#
# class Solution:
#     def Path(self,array,rows,cols,path):
#         if array==None or rows<1 or cols<1 or path==None:
#             return False
#         visited = [0]*(rows*cols)
#
#         pathlength = 0
#         for row in range(rows):
#             for col in range(cols):
#                 if self.haspathcore(array,rows,cols,row,col,path,pathlength,visited):
#                     return True
#         return False
#
#     def haspathcore(self,array,rows,cols,row,col,path,pathlength,visited):
#         if len(array)==pathlength:
#             return True
#         HASPATH = False
#         if row>=0 and row<rows and col>=0 and col<cols and array[row*col+col]==path[pathlength] and \
#             visited[row*cols+col]:
#


#思路：主函数设计从矩阵的每个位置开始调用辅助函数判断以此位置开始是否有这条路径
#辅助函数判断开始位置上下左右移动是否和路径一致，判断边界，出栈之后将路径记录重置

class Solution:
    def hanpath(self,matrix,rows,cols,path):
        if matrix=="" or rows<=0 or cols<=0 or path=="":
            return False
        flag = [0]*len(matrix)
        for i in range(rows):
            if self.findpath(matrix,rows,cols,i,j,path,flag,0):
                return True
        del flag
        return False
    def findpath(self,matrix,rows,cols,i,j,path,flag,0):
        index = i*cols+j
