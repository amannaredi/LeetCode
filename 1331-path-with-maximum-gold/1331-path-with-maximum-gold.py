class Solution:
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxGold = 0

        def inBound(row,col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row,col):
            if not inBound(row,col) or (row,col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row,col))

            left = dfs(row, col-1)
            right = dfs(row , col+1)
            up = dfs(row-1, col)
            down = dfs(row+1 , col)

            visited.remove((row,col))
            return grid[row][col] + max(left,right,up,down)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0 and (row,col) not in visited:
                    maxGold = max(maxGold,dfs(row,col))
        
        return maxGold



        


        
        
                    

        