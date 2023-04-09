from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def exploreIter(grid, r, c, visited):
            if (r,c) in visited:
                return False
            if grid[r][c] == '0':
                return False
            q = deque([(r,c)])
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                appendIfNewAndValidLand(grid, r - 1, c, visited, q)
                appendIfNewAndValidLand(grid, r + 1, c, visited, q)
                appendIfNewAndValidLand(grid, r, c + 1, visited, q)
                appendIfNewAndValidLand(grid, r, c - 1, visited, q)
            return True

        def appendIfNewAndValidLand(grid, r, c, visited, q):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == '1':
                    if (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
        
        visited = set()
        count = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if exploreIter(grid, r, c, visited):
                    count = count + 1
        return count
    
        