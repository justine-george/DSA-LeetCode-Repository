class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]
        for i in range(1, len(nums)):
            cur += nums[i]
            if cur < nums[i]:
                cur = nums[i]
            res = max(res, cur)

        return res