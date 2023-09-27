class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottom up dp with space optimization, T: O(n^2), S: O(n)
        n = len(triangle)
        
        # start filling from bottom row
        # copy last row
        prev_row = triangle[-1][:]
        new_row = [0] * len(prev_row)

        for i in range(len(prev_row) - 2, -1, -1):
            for j in range(i + 1):
                new_row[j] = triangle[i][j] + min(prev_row[j], prev_row[j + 1])

            # at the end, prev_row is the new new_row
            prev_row = new_row[:]

        return prev_row[0]

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