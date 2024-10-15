class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra to find shortest distance from one node to others

        # build an adjacency list
        adj_list = defaultdict(list)
        for u, v, weight in times:
            adj_list[u].append((weight, v))

        q = []
        heapq.heappush(q, (0, k))
        visited = set()
        time_taken = -1
        while q:
            w, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            time_taken = max(time_taken, w)
            for new_w, neighbor in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(q, (w + new_w, neighbor))

        return time_taken if len(visited) == n else -1