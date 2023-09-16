class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # nums.sort()
        
        modMap = {}
        for n in nums:
            mod = n % space
            if mod not in modMap:
                modMap[mod] = 1
            else:
                modMap[mod] += 1
        
        maxModValue = max(modMap.values())
        
        res = float('inf')
        for n in nums:
            if modMap[n % space] == maxModValue and n < res:
                res = n
        return res