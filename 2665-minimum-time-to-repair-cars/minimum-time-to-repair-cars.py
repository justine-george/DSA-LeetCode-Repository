class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks_count = Counter(ranks)

        def check(time):
            cars_repaired = 0
            for rank, freq in ranks_count.items():
                cars_repaired += freq * int(sqrt(time/rank))
            return cars_repaired >= cars
        
        l, r = 1, max(ranks) * cars * cars
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l