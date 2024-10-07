class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # dp
        # recognize base case -> by default, dp[i] = 1
        N = len(arr)
        dp = [1] * N
        sorted_indeces = sorted(range(N), key=lambda i: arr[i])
        
        for i in sorted_indeces:
            # forwards
            for j in range(i + 1, N):
                if arr[j] < arr[i] and abs(i - j) <= d:
                    dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break
            # backwards
            for j in range(i - 1, -1, -1):
                if arr[j] < arr[i] and abs(i - j) <= d:
                    dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break
            
        return max(dp)

        '''
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
        
        def dfs(cur_idx):
            if cur_idx in memo:
                return memo[cur_idx]
            
            max_path = 1
            for neighbor in graph[cur_idx]:
                max_path = max(max_path, 1 + dfs(neighbor))
            
            memo[cur_idx] = max_path
            return max_path
        
        res = 0
        for i in range(N):
            res = max(res, dfs(i))

        return res
        '''