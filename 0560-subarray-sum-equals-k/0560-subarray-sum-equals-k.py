class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 1 1 1
        # 1 2 3 running sum

        # -1    1
        #  0    2 
        #  1     3

        map = {0: 1}

        res = 0
        presum = 0
        for n in nums:
            presum += n
            if presum - k in map:
                res += map[presum - k]
            map[presum] = map.get(presum, 0) + 1
        
        return res