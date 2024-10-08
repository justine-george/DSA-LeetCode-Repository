class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prev_2_prev = 1, 1
        for i in range(2, n + 1):
            cur = prev + prev_2_prev
            prev_2_prev, prev = prev, cur
        return prev

        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]


        # @cache
        # def dfs(i):
        #     if i == n:
        #         return 1
        #     ways = dfs(i + 1) if i + 1 <= n else 0
        #     ways += dfs(i + 2) if i + 2 <= n else 0
        #     return ways

        # return dfs(0)