class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.size = n
        self.adj = defaultdict(list)
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        u, v, cost = edge
        self.adj[u].append((v, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        # djikstra
        # (cost, node)
        heap = [(0, node1)]
        visited = set()

        while heap:
            cost, node = heapq.heappop(heap)
            visited.add(node)

            if node == node2:
                return cost

            for neighbor, cost_to_neighbor in self.adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + cost_to_neighbor, neighbor))
            
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)