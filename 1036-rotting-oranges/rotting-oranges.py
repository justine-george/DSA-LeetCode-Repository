class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([])
        visited = set()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        time_max = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        if grid[nx][ny] == 1:
                            q.append((nx, ny))
                            visited.add((nx, ny))
                            fresh_count -= 1
                            if fresh_count == 0:
                                return time_max + 1

            time_max += 1

        return -1