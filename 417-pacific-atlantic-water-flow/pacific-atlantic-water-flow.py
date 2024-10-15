class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(starts, ocean):
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < ROWS and 0 <= new_c < COLS and
                        not ocean[new_r][new_c] and heights[new_r][new_c] >= heights[r][c]):
                        queue.append((new_r, new_c))
        
        pacific_starts = [(r, 0) for r in range(ROWS)] + [(0, c) for c in range(COLS)]
        atlantic_starts = [(r, COLS - 1) for r in range(ROWS)] + [(ROWS - 1, c) for c in range(COLS)]
        
        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        
        return result