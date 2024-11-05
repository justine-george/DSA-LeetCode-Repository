class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_val = 1

        cur_sum = start_val
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < 1:
                start_val += (1 - cur_sum)
                cur_sum = 1

        return start_val