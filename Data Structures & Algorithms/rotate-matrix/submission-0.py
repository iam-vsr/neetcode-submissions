class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #basically every col, must become a row
        n=len(matrix)

        #transpose a matrix
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for v in matrix:
            v.reverse()


