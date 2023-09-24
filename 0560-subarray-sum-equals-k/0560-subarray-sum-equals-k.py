class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        
        prefix_sum_count_map = {0: 1}
        
        for num in nums:
            cur_sum += num
            res += prefix_sum_count_map.get(cur_sum - k, 0)
            prefix_sum_count_map[cur_sum] = 1 + prefix_sum_count_map.get(cur_sum, 0)
        
        return res