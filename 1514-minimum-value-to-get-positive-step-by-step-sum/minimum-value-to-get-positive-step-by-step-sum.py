class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix_sum = nums[0]
        prefix_sum = nums[0]
        for n in nums[1:]:
            prefix_sum += n
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return 1 - min_prefix_sum if min_prefix_sum < 0 else 1