class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        queue = collections.deque([(0, 0, 0, k - grid[0][0])]) # r, c, steps, k
        visited = set([(0, 0, k - grid[0][0])]) # r, c, k at that point

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, steps_taken, k_remaining = queue.popleft()

            if r == m - 1 and c == n - 1:
                return steps_taken
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n:
                    new_k = k_remaining - grid[new_r][new_c]
                    if new_k >= 0 and (new_r, new_c, new_k) not in visited:
                        queue.append((new_r, new_c, steps_taken + 1, new_k))
                        visited.add((new_r, new_c, new_k))
        
        return -1