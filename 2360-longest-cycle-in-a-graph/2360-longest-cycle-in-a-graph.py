class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        maxLength = -1
        visit = set()
        depth = [float('inf')] * N
        
        def dfs(n, curDepth = 0):
            if n in visit or n == -1:
                return -1
            
            if depth[n] < curDepth:
                return curDepth - depth[n]
            
            depth[n] = curDepth
            val = dfs(edges[n], curDepth + 1)
            visit.add(n)
            return val
            
        for i in range(N):
            maxLength = max(maxLength, dfs(i))
        return maxLength