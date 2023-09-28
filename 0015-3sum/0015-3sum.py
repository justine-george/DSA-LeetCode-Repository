class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers on a sorted array
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            # since array is sorted, and total sum should be 0, first number cannot be positive
            if n > 0:
                break

            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        
        return res