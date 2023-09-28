class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # return [n for n in nums if n % 2 == 0] + [n for n in nums if n % 2 != 0]

        # quicksort-esque solution, inplace sort: T: O(n) since only 1 pass, S: O(1)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 != 0:
                r -= 1
        
        return nums