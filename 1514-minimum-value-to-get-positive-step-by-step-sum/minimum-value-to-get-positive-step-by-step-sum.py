class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # start_val = 1

        # cur_sum = start_val
        # for i in range(len(nums)):
        #     cur_sum += nums[i]
        #     if cur_sum < 1:
        #         start_val += (1 - cur_sum)
        #         cur_sum = 1

        # return start_val

        min_prefix_sum = nums[0]
        prefix_sum = nums[0]
        for n in nums[1:]:
            prefix_sum += n
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return 1 - min_prefix_sum if min_prefix_sum < 0 else 1