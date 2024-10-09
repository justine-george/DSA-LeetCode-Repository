class Solution:
    def __init__(self):
        self.nums = []
    
    @cache
    def dfs(self, curIdx):
        if curIdx >= len(self.nums):
            return 0
        
        skip = self.dfs(curIdx + 1)
        take = self.nums[curIdx] + self.dfs(curIdx + 2)
        
        return max(skip, take)
    
    def rob(self, nums: List[int]) -> int:
        
        self.nums = nums


        return self.dfs(0)