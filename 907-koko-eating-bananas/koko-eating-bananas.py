class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''

        k = banana/hour
        find min k

        time taken to eat all the piles of banana should be <= h

        '''
        def can_eat_all_bananas(speed):
            total_hours = 0
            for pile in piles:
                # total_hours += ceil(pile/speed)
                total_hours += (pile + speed - 1) // speed
            return total_hours <= h

        min_speed, max_speed = 1, max(piles)
        while min_speed < max_speed:
            mid_speed = min_speed + (max_speed - min_speed) // 2
            if can_eat_all_bananas(mid_speed):
                max_speed = mid_speed
            else:
                min_speed = mid_speed + 1
        return min_speed