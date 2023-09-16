class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        
        modCounts = defaultdict(int)
        for n in nums:
            modCounts[n % space] += 1
        
        maxCount = max(modCounts.values())
        
        for n in nums:
            if modCounts[n % space] == maxCount:
                return n