class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[0 if mat[r][c] == 0 else inf for c in range(cols)] for r in range(rows)]
        
        # dp - start from top left
        for r in range(rows):
            for c in range(cols):
                if dist[r][c] != 0:
                    dist[r][c] = 1 + min(dist[r - 1][c] if r - 1 >= 0 else inf, dist[r][c - 1] if c - 1 >= 0 else inf)

        # dp - start from bottom right
        for r in range(rows - 1, -1 , -1):
            for c in range(cols - 1, -1, -1):
                if dist[r][c] != 0:
                    dist[r][c] = min(dist[r][c], 1 + min(dist[r + 1][c] if r + 1 < rows else inf, dist[r][c + 1] if c + 1 < cols else inf))

        return dist

        # rows, cols = len(mat), len(mat[0])
        # dist = [[inf if mat[r][c] else 0 for c in range(cols)] for r in range(rows)]
        # queue = collections.deque([(r, c) for r in range(rows) for c in range(cols) if mat[r][c] == 0])

        # directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        # while queue:
        #     r, c = queue.popleft()
        #     for dr, dc in directions:
        #         new_r, new_c = r + dr, c + dc
        #         if 0 <= new_r < rows and 0 <= new_c < cols:
        #             if dist[new_r][new_c] > dist[r][c] + 1:
        #                 dist[new_r][new_c] = dist[r][c] + 1
        #                 queue.append((new_r, new_c))

        # return dist