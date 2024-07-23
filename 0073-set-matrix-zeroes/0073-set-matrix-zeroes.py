class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        rows = [False]*m
        cols = [False]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 :
                    rows[i], cols[j] = True, True
        print(rows,cols)
        for i,booleen in enumerate(rows):
            if booleen:
                for c in range(n):
                    matrix[i][c] = 0
        for j,c_bool in enumerate(cols):
            if c_bool:
                for r in range(m):
                    matrix[r][j] = 0
            
            
                 

        