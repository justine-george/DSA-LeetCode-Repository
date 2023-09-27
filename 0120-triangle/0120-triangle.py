class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Use a n + 1 size single row, overriding values, best approach
        # bottom up dp with space optimization, T: O(n^2), S: O(n)

        n = len(triangle)
        # initialize prev_row with the last row
        cur_row = [0] * (n + 1)

        # start filling from bottom row
        for i in range(n - 1, -1, -1):
            # for each row, from left to right
            for j in range(i + 1):
                cur_row[j] = triangle[i][j] + min(cur_row[j], cur_row[j + 1])

        return cur_row[0]
        
        # # bottom up dp with space optimization, T: O(n^2), S: O(n)

        # # initialize prev_row with the last row
        # prev_row = triangle[-1][:]
        # new_row = [0] * len(prev_row)

        # # start filling from bottom row
        # for i in range(len(prev_row) - 2, -1, -1):
        #     # for each row, from left to right
        #     for j in range(i + 1):
        #         new_row[j] = triangle[i][j] + min(prev_row[j], prev_row[j + 1])

        #     # at the end, prev_row is the new new_row
        #     prev_row = new_row[:]

        # return prev_row[0]

        # # top down recursion with memoization, T: O(n^2), T: O(n^2)
        # n = len(triangle)
        # dp = {}
        
        # def backtrack(r, c, sum):
        #     if (r, c) in dp:
        #         return dp[(r, c)]
            
        #     # base case: we fell out of the tree
        #     if r == n:
        #         dp[(r, c)] = sum
        #         return sum

        #     dp[(r, c)] = triangle[r][c] + min(backtrack(r + 1, c, sum), backtrack(r + 1, c + 1, sum))
        #     return dp[(r, c)]

        # return backtrack(0, 0, 0)