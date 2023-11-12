class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_taken_heap = [math.ceil(dist[i]/speed[i]) for i in range(n)]
        heapq.heapify(time_taken_heap)

        # res is the time elapsed (also kill_count)
        res = 0
        while time_taken_heap:
            if heapq.heappop(time_taken_heap) <= res:
                break
            res += 1
        return res