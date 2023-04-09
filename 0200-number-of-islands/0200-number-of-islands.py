from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def exploreIter(grid, r, c, visited):
            if (r,c) in visited:
                return False
            if grid[r][c] == '0':
                return False
            st = deque([(r,c)])
            visited.add((r,c))
            while st:
                r, c = st.popleft()
                appendIfNewAndValidLand(grid, r - 1, c, visited, st)
                appendIfNewAndValidLand(grid, r + 1, c, visited, st)
                appendIfNewAndValidLand(grid, r, c + 1, visited, st)
                appendIfNewAndValidLand(grid, r, c - 1, visited, st)
            return True

        def appendIfNewAndValidLand(grid, r, c, visited, st):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == '1':
                    if (r, c) not in visited:
                        st.append((r, c))
                        visited.add((r, c))
        
        visited = set()
        count = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if exploreIter(grid, r, c, visited):
                    count = count + 1
        return count
    
        