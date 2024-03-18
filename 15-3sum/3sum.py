class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        i = 0
        while i < n - 2:
            while 0 < i < n - 2 and nums[i] == nums[i - 1]:
                i += 1

            j = i + 1
            k = n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                
                if cur_sum <= 0:
                    if cur_sum == 0:
                        res.append([nums[i], nums[j], nums[k]])
                    
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j +=1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            
            i += 1
        
        return res