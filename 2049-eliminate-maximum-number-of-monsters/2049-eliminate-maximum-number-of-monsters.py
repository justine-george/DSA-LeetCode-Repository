class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_taken = [math.ceil(dist[i]/speed[i]) for i in range(n)]

        time_taken.sort()

        kill_count = 0
        # i is the time elapsed
        for i in range(n):
            if time_taken[i] <= i:
                return kill_count
            kill_count += 1
        
        return kill_count