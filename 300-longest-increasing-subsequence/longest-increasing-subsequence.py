from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        

        
        # better options
        # T: O(n**2), S: O(n)
        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        
        '''
        # better options
        # T: O(n**2), S: O(n)
        @lru_cache(maxsize=None)
        def dfs(i):
            max_len = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, 1 + dfs(j))

            return max_len
        
        return max(dfs(i) for i in range(len(nums)))
        
        # worst option
        # T: O(n**2), S: O(n**2)
        @cache
        def dfs(i, prev_added_idx):
            if i == len(nums):
                return 0

            # skip
            max_length = dfs(i + 1, prev_added_idx)

            # take
            if prev_added_idx == -1 or nums[i] > nums[prev_added_idx]:
                max_length = max(max_length, 1 + dfs(i + 1, i))
            
            return max_length
        
        return dfs(0, -1)
        '''