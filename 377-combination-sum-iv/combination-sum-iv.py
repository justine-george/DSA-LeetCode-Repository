class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize DP array: dp[i] represents the number of ways to reach sum i
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to reach 0, which is to pick nothing

        # Fill DP array
        for total in range(1, target + 1):
            for num in nums:
                if num <= total:
                    dp[total] += dp[total - num]  # Add ways to reach total - num

        return dp[target]
