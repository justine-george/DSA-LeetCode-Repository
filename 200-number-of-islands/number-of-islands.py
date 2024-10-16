class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if r not in range(m) or c not in range(n) or grid[r][c] == '0' or (r,c) in visited:
                return
            
            visited.add((r, c))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                cur_r, cur_c = q.popleft()

                for dr, dc in directions:
                    new_r, new_c = cur_r + dr, cur_c + dc
                    if new_r in range(m) and new_c in range(n) and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
        
        m, n = len(grid), len(grid[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visited:
                    # dfs(r, c)
                    bfs(r, c)
                    count += 1
        return count