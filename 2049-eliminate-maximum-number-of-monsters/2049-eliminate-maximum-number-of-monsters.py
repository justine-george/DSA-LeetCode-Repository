class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_taken = [dist[i]/speed[i] for i in range(n)]

        time_taken.sort()
        print(time_taken)

        kill_count = 0
        # i is the time elapsed
        for i in range(n):
            if time_taken[i] - i > 0:
                kill_count += 1
            else:
                break
        return kill_count
            
