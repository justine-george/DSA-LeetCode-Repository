class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        rank_count_map = Counter(ranks)
        l = 1
        r = min(rank_count_map) * cars * cars
        while l < r:
            m = l + (r - l) // 2
            if sum((isqrt(m // rank) * rank_count_map[rank]) for rank in rank_count_map) >= cars:
                r = m
            else:
                l = m + 1
        return l
        
        '''
        def check(threshold):
            # rank * n * n = time
            # see if sum of n's obtained from substituting time threshold in the equation above is greater than cars count
            count = 0
            for r in ranks:
                count += int(sqrt(threshold / r))
            return count >= cars
        

        l, r = 1, int(100 * 1e6 * 1e6)
        while l <= r:
            m = l + (r - l) // 2
            # if condition is satisfied, update res and check for an even smaller val
            if check(m):
                r = m - 1
            else:
                l = m + 1

        return l
        '''