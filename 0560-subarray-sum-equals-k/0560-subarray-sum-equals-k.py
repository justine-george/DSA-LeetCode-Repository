class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        
        for num in nums:
            cur_sum += num
            res += prefix_sum_count[cur_sum - k]
            prefix_sum_count[cur_sum] += 1
        
        return res