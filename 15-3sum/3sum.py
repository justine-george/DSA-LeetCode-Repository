class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = set()
        for i in range(n):
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
        
        return res