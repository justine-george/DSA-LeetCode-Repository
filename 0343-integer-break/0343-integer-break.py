class Solution:
    def integerBreak(self, n: int) -> int:
        # Bottom up dp
        # # T: O(n^2), S: O(n)
        # dp value should not be smaller than the n value (except for the last value, n)
        # n  1 2 3 4
        # dp 1 2 3 4
        dp = {1: 1}
        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])
        
        return dp[n]

        # # T: O(n^2), S: O(n)
        # dp = {1: 1}
        # def dfs(num):
        #     if num in dp:
        #         return dp[num]
            
        #     # for the original number n, it's mandatory to break it into smaller integers
        #     dp[num] = 0 if num == n else num
        #     for i in range(1, num):
        #         dp[num] = max(dp[num], dfs(i) * dfs(num - i))
            
        #     return dp[num]
        
        # return dfs(n)