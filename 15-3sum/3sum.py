class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = set()
        i = 0
        while i < n - 2:
            while 0 < i < n - 1 and nums[i] == nums[i - 1]:
                i += 1

            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                sum_loop = nums[j] + nums[k]
                if sum_loop == target:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                elif sum_loop > target:
                    k -= 1
                else:
                    j += 1
            
            i += 1
        
        return res