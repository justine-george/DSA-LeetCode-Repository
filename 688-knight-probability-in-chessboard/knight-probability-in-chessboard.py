class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [
            (-2, 1),
            (-1, 2),
            (-1, -2),
            (-2, -1),
            (2, 1),
            (1, 2),
            (1, -2),
            (2, -1)
        ]

        @cache
        def calculate(move, x, y):
            if move == k:
                return 1.0

            p = 0.0

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    p += calculate(move + 1, nx, ny) / 8.0

            return p
        
        return calculate(0, row, column)