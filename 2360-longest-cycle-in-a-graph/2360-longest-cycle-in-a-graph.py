class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        maxLength = -1
        visited = set()
        node_depth = [-1] * N
        
        def dfs(node, depth):
            if node == -1:
                return 0

            if node in visited:
                return depth - node_depth[node]
            
            if node_depth[node] != -1:
                return 0
            
            visited.add(node)
            node_depth[node] = depth
            cycle_length = dfs(edges[node], depth + 1)
            return cycle_length
        
        for i in range(N):
            maxLength = max(maxLength, dfs(i, 0))
            visited = set()
            
        return maxLength if maxLength > 0 else -1