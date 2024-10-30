class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(time):
            cars_repaired = 0
            for r in ranks:
                cars_repaired += int(sqrt(time/r))
            return cars_repaired >= cars
        
        l, r = 1, int(1e14)
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l