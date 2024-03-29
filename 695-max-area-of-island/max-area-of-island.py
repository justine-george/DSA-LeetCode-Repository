class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        # self.visited = set()
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
        return maxArea

    def dfs(self, grid, i, j):
        # if (i, j) in self.visited:
        #     return 0
        
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return 0
        
        if grid[i][j] == 0:
            return 0
        
        # grid is 1, mark as visited
        # self.visited.add((i, j))
        grid[i][j] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 1
        for dr, dc in directions:
            area += self.dfs(grid, i + dr, j + dc)
        return area
        # return 1 + self.dfs(grid, i + 1, j) + self.dfs(grid, i - 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i, j - 1)
