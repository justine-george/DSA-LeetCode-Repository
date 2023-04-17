class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        l, r = 1, piles[n - 1]
        val = 0
        while l <= r:
            val = l + (r - l) // 2
            
            # check if val rate is koko certified
            totalH = 0
            for r in piles:
                if r % val == 0:
                    totalH += (r / val)
                else:
                    totalH += ((r // val) + 1)
            
            # if less time is needed
            if totalH <= h:
                r = val - 1
            # if more time is needed
            elif totalH > h:
                l = val + 1
        
        return val