class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, length = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                length += 1
            else:
                length = 0
            res += length

        return res