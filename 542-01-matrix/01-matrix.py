class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[inf if mat[r][c] else 0 for c in range(cols)] for r in range(rows)]
        queue = collections.deque([(r, c) for r in range(rows) for c in range(cols) if mat[r][c] == 0])

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if dist[new_r][new_c] > dist[r][c] + 1:
                        dist[new_r][new_c] = dist[r][c] + 1
                        queue.append((new_r, new_c))

        return dist