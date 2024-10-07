class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # graph
        # map: index -> places it can jump to
        # DFS memoize

        graph = defaultdict(set)
        memo = {}

        N = len(arr)

        # build adjacency list
        for i in range(N):
            for j in range(i + 1, N):
                if arr[j] < arr[i] and abs(j - i) <= d:
                    graph[i].add(j)
                else:
                    break
            for j in range(i - 1, -1, -1):
                if arr[j] < arr[i] and abs(j - i) <= d:
                    graph[i].add(j)
                else:
                    break
        
        def dfs(cur_idx, N):
            if cur_idx == N:
                return 0
            
            if cur_idx in memo:
                return memo[cur_idx]
            
            path = 1
            for neighbor in graph[cur_idx]:
                path = max(path, 1 + dfs(neighbor, N))
            memo[cur_idx] = path
            return path
        
        res = 0
        for i in range(N):
            res = max(res, dfs(i, N))
        return res
    
    # def dfs(self, cur_idx, N):
    #     if cur_idx == N:
    #         return 0
        
    #     if cur_idx in self.memo:
    #         return self.memo[cur_idx]
        
    #     path = 1
    #     for neighbor in self.graph[cur_idx]:
    #         path = max(path, 1 + self.dfs(neighbor, N))
    #     self.memo[cur_idx] = path
    #     return path