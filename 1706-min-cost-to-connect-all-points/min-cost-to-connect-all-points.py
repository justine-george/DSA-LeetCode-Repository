class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        min_heap = [(0, 0)]  # (cost, point_index)
        in_mst = set()
        total_cost = 0

        while len(in_mst) < N:
            cost, i = heapq.heappop(min_heap)
            if i in in_mst:
                continue
            
            total_cost += cost
            in_mst.add(i)

            for j in range(N):
                if j not in in_mst:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    manh_dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (manh_dist, j))

        return total_cost