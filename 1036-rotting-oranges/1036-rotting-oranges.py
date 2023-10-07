class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi source BFS
        Take count of fresh oranges and add rotten oranges to a queue
        While queue is non empty and fresh > 0:
            iterate over every currently rotten orange:
                popleft and get a rotten orange:
                    spread to each of the 4-directions
                    rot the fresh orange
                    add this newly rotten orange to the queue
            increment time
        return time if all fresh oranges are rotten, else not possible
        """
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])
        time_taken, count_fresh = 0, 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count_fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and count_fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    count_fresh -= 1
            time_taken += 1
        return time_taken if count_fresh == 0 else -1