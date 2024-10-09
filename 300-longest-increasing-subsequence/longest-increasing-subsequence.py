class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     for j in range(0, i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], 1 + dp[j])

        # return max(dp)

        @cache
        def dfs(i):
            max_len = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, 1 + dfs(j))

            return max_len
        
        return max(dfs(i) for i in range(len(nums)))
        
        # # T: O(n**2), S: O(n**2)
        # @cache
        # def dfs(i, prev_added_idx):
        #     if i == len(nums):
        #         return 0

        #     # skip
        #     max_length = dfs(i + 1, prev_added_idx)

        #     # take
        #     if prev_added_idx == -1 or nums[i] > nums[prev_added_idx]:
        #         max_length = max(max_length, 1 + dfs(i + 1, i))
            
        #     return max_length
        
        # return dfs(0, -1)