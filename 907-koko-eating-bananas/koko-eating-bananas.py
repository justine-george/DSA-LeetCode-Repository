class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k, ie. speed ranges from l to r. Find min k
        l, r = 1, max(piles)
        self.allowed_time = h
        self.piles = piles

        while l < r:
            m = l + (r - l) // 2
            if self.is_condition(m):
                r = m
            else:
                l = m + 1
        return l
    
    def is_condition(self, k):
        time_taken = sum( ceil(pile_count / k) for pile_count in self.piles)
        return time_taken <= self.allowed_time