class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        cur_sum = 0
        for i, n in enumerate(nums):
            # avoid divisions when the numbers could be negative
            if cur_sum == total - n - cur_sum:
                return i
            cur_sum += n
            
        return -1