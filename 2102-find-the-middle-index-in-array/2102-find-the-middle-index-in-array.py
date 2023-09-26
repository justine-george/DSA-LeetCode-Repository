class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        running_sum = 0
        for i, n in enumerate(nums):
            if running_sum == total - n - running_sum:
                return i
            running_sum += n
        
        return -1