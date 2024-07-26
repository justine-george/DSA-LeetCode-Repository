from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for st, end, dist in edges:
            graph[st].append((dist, end))
            graph[end].append((dist, st))   
        
        res_map = {i: 0 for i in range(n)}
        for i in range(n):
            visited = set()
            pq = [(0, i)]
            heapq.heapify(pq)
            while pq:
                current_dist, node = heapq.heappop(pq)
                visited.add(node)
                for dist, neighbor in graph[node]:
                    if neighbor not in visited and dist+current_dist <= distanceThreshold:
                        heapq.heappush(pq, (dist+current_dist, neighbor))
            
            res_map[i] = len(visited) - 1
        
        min_node, min_val = 0, float('inf')
        for i in res_map:
            val = res_map[i]
            if val <= min_val:
                min_val = val
                min_node = i

        return min_node