class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def count(grid, r, c, char):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return " "
            
            grid[r][c] = 0

            res = char
            directions = [(1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l')]
            for dr, dc, direc in directions:
                res += count(grid, r + dr, c + dc, direc)
            
            return res

        shapes = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    shape = count(grid, r, c, 's')
                    print(shape)
                    shapes.add(shape)
        
        return len(shapes)