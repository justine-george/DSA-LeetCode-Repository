class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        count = 0
        i = 0
        while i < n - 2:
            j = i + 1
            k = n - 1
            
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                
                if cur_sum < target:
                    # no need to k -= 1, since numbers below nums[k] and above nums[j] will be less than nums[k], thus satisfying this condition, so k - j numbers.
                    count += k - j
                    j += 1
                else:
                    k -= 1
        
            i += 1

        return count