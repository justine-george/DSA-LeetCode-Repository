class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''

        k = banana/hour
        find min k

        time taken to eat all the piles of banana should be <= h

        '''
        piles_count = Counter(piles)

        def check(speed):
            time_taken = 0
            for p, freq in piles_count.items():
                # time_taken += ceil(p/speed)
                time_taken += freq * ((p + speed - 1) // speed)
                if time_taken > h:
                    return False
            return time_taken <= h

        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l