class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        cur_sum = 0
        for i, n in enumerate(nums):
            if (total - n - cur_sum) == cur_sum:
                return i
            cur_sum += n
            
        return -1