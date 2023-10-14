class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        res = 0
        presum = 0
        for n in nums:
            presum += n
            if presum - k in map:
                res += map[presum - k]
            map[presum] = map.get(presum, 0) + 1
        return res