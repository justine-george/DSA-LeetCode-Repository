from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isUnseenIsland(r, c):
            q = deque([(r,c)])
            visited.add((r,c))
            
            while q:
                curR, curC = q.popleft()
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr, dc in directions:
                    newR, newC = curR + dr, curC + dc
                    validateAndAddLand(newR, newC, q)

        def validateAndAddLand(r, c, q):
            if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == '1' and (r,c) not in visited:
                    isUnseenIsland(r, c)
                    count += 1
        return count
        
#         # Below solution is only valid if input grid can be mutated
#         # when visited, change value to -1
#         # T: O(m*n), S: O(min(m,n)) for bfs queue
#         def isUnseenIsland(r, c):
#             q = deque([(r,c)])
#             grid[r][c] = -1
            
#             while q:
#                 curR, curC = q.popleft()
#                 directions= [[1,0],[-1,0],[0,1],[0,-1]]
                
#                 for dr, dc in directions:
#                     newR, newC = curR + dr, curC + dc
#                     validateAndAddLand(newR, newC, q)

#         def validateAndAddLand(r, c, q):
#             if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and grid[r][c] != -1):
#                         q.append((r, c))
#                         grid[r][c] = -1
        
#         rows, cols = len(grid), len(grid[0])
#         count = 0
#         for r, row in enumerate(grid):
#             for c, _ in enumerate(row):
#                 if grid[r][c] == '1' and grid[r][c] != -1:
#                     isUnseenIsland(r, c)
#                     count += 1
#         return count