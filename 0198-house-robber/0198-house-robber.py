class Solution:
    def rob(self, nums: List[int]) -> int:
        # # top down recursive - memoization
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

        # # iterative
        # dp = [0] * (len(nums) + 1)
        # dp[-2] = nums[-1]
        # for i in range(len(nums) - 2, -1, -1):
        #     dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        # return dp[0]

        # most space efficient, O(1)
        next_to_next = 0
        next = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            val = max(nums[i] + next_to_next, next)
            next_to_next = next
            next = val

        return next