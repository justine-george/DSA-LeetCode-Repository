class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        maxLength = -1
        visited = set()    # To track nodes that are currently being visited in DFS
        node_depth = [-1] * N  # To store the depth of each node
        
        def dfs(node, depth):
            # If node is terminal or already processed in previous DFS
            if node == -1:
                return 0

            # If node is currently being visited, we detected a cycle
            if node in visited:
                return depth - node_depth[node]
            
            # If we've visited this node in a different DFS before
            if node_depth[node] != -1:
                return 0
            
            visited.add(node)
            node_depth[node] = depth
            
            cycle_length = dfs(edges[node], depth + 1)
            
            # visited.remove(node)
            return cycle_length
        
        for i in range(N):
            maxLength = max(maxLength, dfs(i, 0))
            visited = set()
            
        return maxLength if maxLength > 0 else -1
