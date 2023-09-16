class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        
        modCounts = defaultdict(int)
        modSmallest = defaultdict(lambda: float('inf'))
        
        for n in nums:
            mod = n % space
            modCounts[mod] += 1
            modSmallest[mod] = min(modSmallest[mod], n)
        
        maxCountMod = max(modCounts, key=modCounts.get)
        
        return modSmallest[maxCountMod]