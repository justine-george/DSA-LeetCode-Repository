class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        count = 0
        i = 0
        while i < n - 2:
            # while 0 < i < n - 2 and nums[i] == nums[i - 1]:
            #     i += 1

            j = i + 1
            k = n - 1
            
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                
                if cur_sum < target:  # If the current sum is less than the target, all elements from j to k are valid
                    count += k - j  # Add all possible third numbers with the current first and second numbers
                    j += 1  # Move the second number pointer forward
                else:
                    k -= 1
        
            i += 1

        return count