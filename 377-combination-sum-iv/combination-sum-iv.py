class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # bottom-up dp
        # T: O(n . m), n is target number, m is len(nums)
        # S: O(n)
        dp = {0: 1}

        for total in range(1, target + 1):
            dp[total] = 0
            # dp[target] =
            #     dp[target - nums[0]] (choose ith nums element) + 
            #     .. + 
            #     dp[target - nums[i]] + 
            #     .. + 
            #     choose last nums element too.
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        
        return dp[target]

        # memoized recursion
        # T: O(n . m), n is target number, m is len(nums)
        # S: O(n)
        # self.dp = {}

        # def dfs(total):
        #     if total in self.dp:
        #         return self.dp[total]

        #     if total == target:
        #         return 1
            
        #     if total > target:
        #         return 0

        #     count = 0
        #     for n in nums:
        #         count += dfs(total + n)

        #     self.dp[total] = count
        #     return count
        
        # return dfs(0)