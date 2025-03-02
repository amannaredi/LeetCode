class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    numIslands += 1
        return numIslands

    def dfs(self,grid,r,c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!= "1" :
            return
        
        grid[r][c] = "0"
        
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)