class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2
            
            # check if val rate is koko certified
            totalH = 0
            for p in piles:
                totalH += math.ceil(p / k)
            
            # if less or exact time is needed
            if totalH <= h:
                res = min(res, k)
                r = k - 1
            # if more time is needed
            elif totalH > h:
                l = k + 1
        
        return res