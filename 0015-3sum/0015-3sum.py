class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]: # skip the duplicates
                continue
    
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                sum = val + nums[l] + nums[r]
                
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
                    