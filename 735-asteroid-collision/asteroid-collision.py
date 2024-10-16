class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            while res and res[-1] > 0 and asteroid < 0:
                if abs(asteroid) > res[-1]:
                    res.pop()
                elif abs(asteroid) < res[-1]:
                    asteroid = 0
                else:
                    res.pop()
                    asteroid = 0

            if asteroid != 0:
                res.append(asteroid)
            
        return res