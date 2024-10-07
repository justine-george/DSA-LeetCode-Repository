class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # graph
        # map: index -> places it can jump to
        # DFS memoize

        self.graph = defaultdict(set)
        self.memo = {}

        N = len(arr)

        # build adjacency list
        for i in range(N):
            for j in range(i + 1, N):
                if arr[j] < arr[i] and abs(j - i) <= d:
                    self.graph[i].add(j)
                else:
                    break
            for j in range(i - 1, -1, -1):
                if arr[j] < arr[i] and abs(j - i) <= d:
                    self.graph[i].add(j)
                else:
                    break
        
        res = 0
        for i in range(N):
            res = max(res, self.dfs(i, N))
        return res
    
    def dfs(self, cur_idx, N):
        if cur_idx == N:
            return 0
        
        if cur_idx in self.memo:
            return self.memo[cur_idx]
        
        path = 1
        for neighbor in self.graph[cur_idx]:
            path = max(path, 1 + self.dfs(neighbor, N))
        self.memo[cur_idx] = path
        return path