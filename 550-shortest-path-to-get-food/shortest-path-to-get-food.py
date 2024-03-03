class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = collections.deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    queue.append((row, col, 0))
                    visited.add((row, col))

                    break
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            cur_row, cur_col, steps = queue.popleft()

            if grid[cur_row][cur_col] == '#':
                return steps
            else:
                for row_incr, col_incr in directions:
                    new_row = cur_row + row_incr
                    new_col = cur_col + col_incr

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != 'X':
                        if (new_row, new_col) not in visited:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col, steps + 1))
            
        return -1








["X","X","X","X","X","X"]
["X","*","O","O","O","X"]
["X","O","O","#","O","X"]
["X","X","X","X","X","X"]