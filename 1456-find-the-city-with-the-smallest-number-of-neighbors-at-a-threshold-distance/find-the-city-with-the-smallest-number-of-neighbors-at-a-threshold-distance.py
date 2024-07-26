from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for st, end, dist in edges:
            graph[st].append((dist, end))
            graph[end].append((dist, st))
        
        # floyd-warshall algorithm: all point shortest
        # distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for st, end, distance in edges:
            dist[st][end] = distance
            dist[end][st] = distance

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        min_node, min_count = 0, float('inf')
        for i in range(n):
            valid_count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    valid_count += 1
            
            if valid_count <= min_count:
                min_count = valid_count
                min_node = i
        
        return min_node

        # res_map = {i: 0 for i in range(n)}
        # for i in range(n):
        #     visited = set()
        #     pq = [(0, i)]
        #     while pq:
        #         current_dist, node = heapq.heappop(pq)
        #         visited.add(node)
        #         for dist, neighbor in graph[node]:
        #             if neighbor not in visited and dist+current_dist <= distanceThreshold:
        #                 heapq.heappush(pq, (dist+current_dist, neighbor))
            
        #     res_map[i] = len(visited) - 1
        
        # min_node, min_val = 0, float('inf')
        # for i in res_map:
        #     val = res_map[i]
        #     if val <= min_val:
        #         min_val = val
        #         min_node = i

        # return min_node