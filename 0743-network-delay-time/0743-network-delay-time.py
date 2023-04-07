class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # O(ELogV) time complexity
        adjList = collections.defaultdict(list)
        
        # create adjacency list
        for u, v, weight in times:
            adjList[u].append((v, weight))
        
        # (pathlength, destNode), heapq will sort by the first element of the tuple
        minHeap = [(0, k)] # starting from k
        visit = set()
        t = 0 # cost to visit the last node
        
        while minHeap:
            pathLength, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            t = max(t, pathLength)
            
            for v, weight in adjList[node]:
                if v not in visit:
                    heapq.heappush(minHeap, (pathLength + weight, v))
        
        return t if len(visit) == n else -1