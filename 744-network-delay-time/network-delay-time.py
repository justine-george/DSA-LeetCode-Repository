class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra to find shortest distance from one node to others

        # Build an adjacency list
        adj_list = defaultdict(list)
        for u, v, weight in times:
            adj_list[u].append((weight, v))
            
        # Initialize the min heap
        q = [(0, k)]
        
        # Distance dictionary
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        
        while q:
            curr_dist, node = heapq.heappop(q)
            
            if curr_dist > dist[node]:
                continue
            
            for new_w, neighbor in adj_list[node]:
                new_dist = curr_dist + new_w
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(q, (new_dist, neighbor))
        
        max_dist = max(dist.values())
        return max_dist if max_dist < float('inf') else -1