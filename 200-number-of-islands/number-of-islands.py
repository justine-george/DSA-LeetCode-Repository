class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islandCount = 0
        self.m, self.n = len(grid), len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if int(grid[i][j]) == 1:
                    self.dfs(grid, i, j)
                    self.islandCount += 1
        
        return self.islandCount
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return

        if grid[i][j] == '0':
            return

        # mark as visited
        grid[i][j] = '0'


        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)