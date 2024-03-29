class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # T: O(nlog(n))
        maxPile = max(piles)
        if len(piles) == h:
            return maxPile
        
        # try values between these as rates
        l, r = math.ceil(sum(piles) / h), maxPile 
        res = r
        while l <= r:
            k = l + (r - l) // 2
            
            # find out total hours for koko to finish the piles in k rate
            totalH = 0
            for p in piles:
                totalH += math.ceil(p / k)
            
            # if less or exact time is needed
            if totalH <= h:
                res = k
                r = k - 1
            # if more time is needed
            else:
                l = k + 1
        
        return res