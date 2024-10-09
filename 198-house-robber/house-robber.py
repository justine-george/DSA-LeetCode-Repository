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
        self.nums = nums
        return self.dfs(0)