import copy
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [
            (-2,-1),
            (-2,1),
            (-1,-2),
            (-1,2),
            (1,-2),
            (1,2),
            (2,-1),
            (2,1),
        ]

        # bottoms up approach - space optimized
        # initialize 2 2d dps
        prev_dp = [[0.0 for _ in range(n)] for _ in range(n)]
        cur_dp = [[0.0 for _ in range(n)] for _ in range(n)]

        # base case: 0 moves -> prob = 1 if starting on the board
        for i in range(n):
            for j in range(n):
                prev_dp[i][j] = 1.0
        
        # fill dp table
        for move in range(1, k + 1):
            for x in range(n):
                for y in range(n):
                    cur_dp[x][y] = 0.0
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            cur_dp[x][y] += prev_dp[nx][ny] / 8.0
            prev_dp, cur_dp = cur_dp, prev_dp

        return prev_dp[row][column]

        # # bottoms up approach
        # # initialize 3d dp with all zeros
        # dp = [[[0.0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]

        # # base case: 0 moves -> prob = 1 if starting on the board
        # for i in range(n):
        #     for j in range(n):
        #         dp[0][i][j] = 1.0
        
        # # fill dp table
        # for move in range(1, k + 1):
        #     for x in range(n):
        #         for y in range(n):
        #             for dx, dy in directions:
        #                 nx, ny = x + dx, y + dy
        #                 if 0 <= nx < n and 0 <= ny < n:
        #                     dp[move][x][y] += dp[move - 1][nx][ny] / 8.0

        # print(dp)
        # return dp[k][row][column]

        # recursive dp + memoization
        # dp = {}
        # def calculate(move, x, y):
        #     if (move, x, y) in dp:
        #         return dp[(move, x, y)]

        #     if move == k:
        #         return 1.0

        #     p = 0.0

        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy

        #         if 0 <= nx < n and 0 <= ny < n:
        #             p += calculate(move + 1, nx, ny) / 8.0

        #     dp[(move, x, y)] = p
        #     return p
        
        # return calculate(0, row, column)