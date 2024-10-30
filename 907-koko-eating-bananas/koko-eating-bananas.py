class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''

        k = banana/hour
        find min k

        time taken to eat all the piles of banana should be <= h

        '''
        def check(speed):
            time_taken = 0
            for p in piles:
                time_taken += ceil(p/speed)
            return time_taken <= h

        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l