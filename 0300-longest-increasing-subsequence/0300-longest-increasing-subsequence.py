class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        # LIS starting from index i idea - bottom up, iterate in reverse

        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            maxLen = -1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxLen = max(maxLen, 1 + dp[j])
                else:
                    maxLen = max(maxLen, 1)
            dp[i] = maxLen
        
        return max(dp)