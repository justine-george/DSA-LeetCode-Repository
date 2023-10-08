class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # dp: T: O(n^2), S: O(n)
        # # LIS starting from index i idea - bottom up, iterate in reverse

        # dp = [1] * len(nums)
        # for i in range(len(nums) - 2, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        
        # # LIS could start from any index
        # return max(dp)


        # dp: T: O(n^2), S: O(n)
        # LIS ending at index i idea - bottom up, iterate from the start

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # LIS could start from any index
        return max(dp)