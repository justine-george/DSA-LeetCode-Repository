class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        min_cost = [float('inf')] * N
        min_cost[0] = 0 # starting from 1st point
        connected = set()
        total_cost = 0

        for _ in range(N):
            cur_min_cost = float('inf')
            cur_min_point = -1

            # Find the next point to connect to MST
            for i in range(N):
                if i not in connected and min_cost[i] < cur_min_cost:
                    cur_min_cost = min_cost[i]
                    cur_min_point = i
            
            # Add the selected point to MST
            total_cost += cur_min_cost
            connected.add(cur_min_point)

            # Update the cost array with paths from the current point
            cur_x, cur_y = points[cur_min_point]
            for j in range(N):
                if j not in connected:
                    x, y = points[j]
                    manh_dist = abs(x - cur_x) + abs(y - cur_y)
                    if manh_dist < min_cost[j]:
                        min_cost[j] = manh_dist

        return total_cost