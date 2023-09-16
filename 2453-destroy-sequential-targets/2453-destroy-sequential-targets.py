class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
#         nums.sort()
#         # nums[i], count
#         res = [0, 0]
#         for i in range(len(nums)):
#             count = 1
#             for j in range(i + 1, len(nums)):
#                 diff = nums[j] - nums[i]
#                 if diff % space == 0:
#                     count += 1
#             if count == res[1]:
#                 if nums[i] < res[0]:
#                     res[0] = nums[i]
#             elif count > res[1]:
#                 res[0] = nums[i]
#                 res[1] = count
        
#         return res[0]
    
        nums.sort()
        
        modCounts = defaultdict(int)
        for n in nums:
            modCounts[n % space] += 1
        
        maxCount = max(modCounts.values())
        
        for n in nums:
            if modCounts[n % space] == maxCount:
                return n