class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n



        @cache
        def dfs(i):
            if i == n:
                return 1
            ways = dfs(i + 1) if i + 1 <= n else 0
            ways += dfs(i + 2) if i + 2 <= n else 0
            return ways

        return dfs(0)
