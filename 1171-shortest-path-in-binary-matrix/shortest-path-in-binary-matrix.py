class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n -1] == 1:
            return -1

        q = collections.deque([(0, 0, 1)])
        grid[0][0] = -1 # mark as visited on the grid itself

        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
        while q:
            r, c, length = q.popleft()
            
            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
                    q.append((new_r, new_c, length + 1))
                    grid[new_r][new_c] = -1
        
        return -1

        # n = len(grid)

        # if grid[0][0] == 1 or grid[n - 1][n -1] == 1:
        #     return -1

        # q = collections.deque([(0, 0, 1)])
        # visited = set([(0, 0)])

        # directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
        # while q:
        #     r, c, length = q.popleft()
            
        #     if r == n - 1 and c == n - 1:
        #         return length

        #     for dr, dc in directions:
        #         new_r, new_c = r + dr, c + dc
        #         if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0 and (new_r, new_c) not in visited:
        #             q.append((new_r, new_c, length + 1))
        #             visited.add((new_r, new_c))
        
        # return -1