class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # cost, points index
        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0

        while min_heap:
            cost, index = heapq.heappop(min_heap)
            
            if index in visited:
                continue
            
            total_cost += cost
            visited.add(index)

            cur_x, cur_y = points[index]
            # completely connected graph, all other points are neighbors
            for i, point in enumerate(points):
                x, y = point
                # if i not in visited:
                manh_dist = abs(cur_x - x) + abs(cur_y - y)
                heapq.heappush(min_heap, (manh_dist, i))
        
        return total_cost