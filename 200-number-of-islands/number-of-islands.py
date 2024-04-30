class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return

            # if grid[r][c] == '0':
            #     return
            
            grid[r][c] = '0'
            
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        m, n = len(grid), len(grid[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count