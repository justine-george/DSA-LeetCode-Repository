class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = {}

        # def dp(i):
        #     if i in memo:
        #         return memo[i]

        #     if i >= len(nums):
        #         memo[i] = 0
        #         return 0

        #     memo[i] = max(
        #         nums[i] + dp(i + 2),
        #         dp(i + 1)
        #     )
        #     return memo[i]
        
        # return dp(0)

        # space efficient
        dp = [0] * (len(nums) + 1)
        dp[-2] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]