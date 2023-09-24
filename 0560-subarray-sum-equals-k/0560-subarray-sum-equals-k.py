class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            res += prefix_sum_count[cur_sum - k]
            prefix_sum_count[cur_sum] += 1
        
        return res