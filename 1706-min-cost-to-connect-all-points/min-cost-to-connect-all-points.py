class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        # completely connected graph, all other points are neighbors
        # { i: [(dist, j)]} means i->j costs dist
        adj = { i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                manh_dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append((manh_dist, j))
                adj[j].append((manh_dist, i))
        
        # prim's algorithm
        visited = set()
        total_cost = 0
        # cost, points index
        min_heap = [(0, 0)]

        while len(visited) < N:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            
            total_cost += cost
            visited.add(i)

            for neiCost, nei in adj[i]:
                # if nei not in visited:
                heapq.heappush(min_heap, (neiCost, nei))
        
        return total_cost