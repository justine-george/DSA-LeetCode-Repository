class Solution:
    def __init__(self):
        self.nums = []
        self.memo = {}
    
    def dfs(self, curIdx):
        if curIdx >= len(self.nums):
            return 0

        if curIdx in self.memo:
            return self.memo[curIdx]
        
        skip = self.dfs(curIdx + 1)
        take = self.nums[curIdx] + self.dfs(curIdx + 2)
        
        self.memo[curIdx] = max(skip, take)
        return self.memo[curIdx]
    
    def rob(self, nums: List[int]) -> int:
        # self.nums = nums
        # return self.dfs(0)
        
        # dp = [0] * (len(nums) + 2)
        # for i in range(len(nums) - 1, -1, -1):
        #     dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        # return dp[0]

        next, next2next = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            cur = max(next, nums[i] + next2next)
            next2next, next = next, cur
        return next
