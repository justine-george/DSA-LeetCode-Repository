class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        self.rank_counter = Counter(ranks)
        l, r = 1, int(min(ranks) * cars * cars)
        
        while l < r:
            m = l + (r - l) // 2
            # if condition is satisfied, update res and check for an even smaller val
            if self.check(cars, m):
                r = m
            else:
                l = m + 1

        return l
    
    def check(self, cars, threshold):
        # rank * n * n = time
        # see if sum of n's obtained from substituting time threshold in the equation above is greater than cars count
        count = 0
        for rank, freq in self.rank_counter.items():
            count += int(sqrt(threshold / rank)) * freq
        return count >= cars