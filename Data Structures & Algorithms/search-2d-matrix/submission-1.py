class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr=0
        rr=len(matrix)-1

        l=0
        r=len(matrix[0])-1

        while lr<=rr:
            mr=rr-(rr-lr)//2
            if matrix[mr][0]<=target and matrix[mr][-1]>=target:
                while l<=r:
                    m=r-(r-l)//2
                    if matrix[mr][m]==target:
                        return True
                    elif matrix[mr][m]>target:
                        r=m-1
                    else:
                        l=m+1
                return False
                
            elif matrix[mr][0]<target and matrix[mr][-1]<target:
                lr=mr+1
            else:
                rr=mr-1
        
        return False
                
            