class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum_count_map = {0: 1} # 0 sum is possible in a single way, by not including anything, base case 
        cur_sum = 0
        res = 0
        for n in nums:
            cur_sum += n
            # idea: can we chop off a prefix to get the required target sum of k?
            if cur_sum - k in prefixsum_count_map:
                res += prefixsum_count_map[cur_sum - k]
            prefixsum_count_map[cur_sum] = 1 + prefixsum_count_map.get(cur_sum, 0)
        
        return res