class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid1), len(grid1[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        def dfs(i, j):
            if i not in range(m) or j not in range(n) or (i, j) in visited or grid2[i][j] == 0:
                return True
            visited.add((i, j))

            res = True
            if grid1[i][j] == 0:
                res = False
            for dx, dy in directions:
                res = dfs(i + dx, j + dy) and res

            return res

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited and dfs(i, j):
                    count += 1
        
        return count