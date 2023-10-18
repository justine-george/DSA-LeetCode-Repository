class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for src, dest in relations:
            adj[src].append(dest)

        max_time = {} # src - >  max_time
        def dfs(src):
            if src in max_time:
                return max_time[src]

            max_time[src] = time[src - 1]
            for n in adj[src]:
                max_time[src] = max(max_time[src], time[src - 1] + dfs(n))

            return max_time[src]

        for i in range(1, n + 1):
            dfs(i)
        
        return max(max_time.values())