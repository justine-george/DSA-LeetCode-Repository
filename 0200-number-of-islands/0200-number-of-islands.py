from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if self.exploreIter(grid, r, c, visited):
                    count = count + 1
        return count
    
    def exploreIter(self, grid, r, c, visited):
        if (r,c) in visited:
            return False
        if grid[r][c] == '0':
            return False
        st = deque()
        st.append((r,c))
        visited.add((r,c))
        while len(st) != 0:
            r, c = st.popleft()
            self.appendIfNewAndValidLand(grid, r - 1, c, visited, st)
            self.appendIfNewAndValidLand(grid, r + 1, c, visited, st)
            self.appendIfNewAndValidLand(grid, r, c + 1, visited, st)
            self.appendIfNewAndValidLand(grid, r, c - 1, visited, st)
        return True

    def appendIfNewAndValidLand(self, grid, r, c, visited, st):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == '1':
                if (r, c) not in visited:
                    st.append((r, c))
                    visited.add((r, c))