class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        min_cost = [math.inf] * N  # to track the minimum connection cost to MST for each point
        min_cost[0] = 0  # starting from the first point
        connected = set()
        total_cost = 0

        for _ in range(N):
            curr_min_cost = math.inf
            curr_point = -1

            # Find the next point to connect to the MST
            for i in range(N):
                if i not in connected and min_cost[i] < curr_min_cost:
                    curr_min_cost = min_cost[i]
                    curr_point = i

            # Add the selected point to MST
            total_cost += curr_min_cost
            connected.add(curr_point)

            # Update the cost array with paths from the current point
            curr_x, curr_y = points[curr_point]
            for j in range(N):
                if j not in connected:
                    x, y = points[j]
                    manh_dist = abs(x - curr_x) + abs(y - curr_y)
                    if manh_dist < min_cost[j]:
                        min_cost[j] = manh_dist

        return total_cost