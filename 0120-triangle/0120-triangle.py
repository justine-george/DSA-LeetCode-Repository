class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = {}
        def backtrack(r, c, sum):
            if (r, c) in dp:
                return dp[(r, c)]
            
            # base case: we fell out of the tree
            if r == n:
                dp[(r, c)] = sum
                return sum

            dp[(r, c)] = triangle[r][c] + min(backtrack(r + 1, c, sum), backtrack(r + 1, c + 1, sum))
            return dp[(r, c)]
        
        return backtrack(0, 0, 0)