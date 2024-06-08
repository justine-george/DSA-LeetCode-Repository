class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cum_sum_map = {0: -1}

        s = 0
        for i, n in enumerate(nums):
            s += n
            if k != 0:
                s = s % k

            if s in cum_sum_map:
                if i - cum_sum_map[s] > 1:
                    return True
            else:
                cum_sum_map[s] = i
        
        return False