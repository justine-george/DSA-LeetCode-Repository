class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T: O(n^2), S: O(1)
        res = []
        nums.sort() 
        
        # for each element, take the sorted elements to the right and 
        # use two pointer to find sum (two sum II) 
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]: # skip the duplicates
                continue
    
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                sum = val + nums[l] + nums[r]
                
                if sum == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: # skip the duplicates
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res