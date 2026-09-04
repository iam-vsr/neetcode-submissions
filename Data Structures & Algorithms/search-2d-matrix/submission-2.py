# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         lr=0
#         rr=len(matrix)-1

#         l=0
#         r=len(matrix[0])-1

#         while lr<=rr:
#             mr=rr-(rr-lr)//2
#             if matrix[mr][0]<=target and matrix[mr][-1]>=target:
#                 while l<=r:
#                     m=r-(r-l)//2
#                     if matrix[mr][m]==target:
#                         return True
#                     elif matrix[mr][m]>target:
#                         r=m-1
#                     else:
#                         l=m+1
#                 return False
                
#             elif matrix[mr][0]<target and matrix[mr][-1]<target:
#                 lr=mr+1
#             else:
#                 rr=mr-1
        
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])

        l=0
        r=rows*cols-1

        while l<=r:
            m=r-(r-l)//2
            row, col = m//cols, m%cols
            if target>matrix[row][col]:
                l=m+1
            elif target<matrix[row][col]:
                r=m-1
            else:
                return True
        return False
                
            