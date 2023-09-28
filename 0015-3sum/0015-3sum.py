class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T: O(n^2), S: O(1) (excluding sort O(n) space)
        nums.sort()
        res = []

        for i in range(len(nums)):
            # since array is sorted, and total sum should be 0, first number cannot be positive
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res