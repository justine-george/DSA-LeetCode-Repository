class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            if grid[0][0] == 1 and grid[m - 1][n - 1] == 1:
                if k < 2:
                    return -1
            elif grid[0][0] == 1:
                if k < 1:
                    return -1
            else:
                if k < 1:
                    return -1

        queue = collections.deque([(0, 0, 0, k)]) # r, c, steps, k
        if grid[0][0] == 1:
            k -= 1
        visited = set([(0, 0, k)]) # r, c, k at that point

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        min_steps = inf
        while queue:
            r, c, steps_taken, k_remaining = queue.popleft()

            if r == m - 1 and c == n - 1:
                min_steps = min(min_steps, steps_taken)
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < m and 0 <= new_c < n:
                    if grid[new_r][new_c] == 1:
                        if k_remaining >= 1 and (new_r, new_c, k_remaining - 1) not in visited:
                            queue.append((new_r, new_c, steps_taken + 1, k_remaining - 1))
                            visited.add((new_r, new_c, k_remaining - 1))
                    else:
                        if (new_r, new_c, k_remaining) not in visited:
                            queue.append((new_r, new_c, steps_taken + 1, k_remaining))
                            visited.add((new_r, new_c, k_remaining))
        
        return -1 if min_steps == inf else min_steps



