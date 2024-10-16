class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_so_far = float('-inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k:
                    max_so_far = max(max_so_far, nums[i] + nums[j])

        return max_so_far if max_so_far != float('-inf') else -1