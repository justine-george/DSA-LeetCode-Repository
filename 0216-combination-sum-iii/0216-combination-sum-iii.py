class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        candidates = [i for i in range(1, 10)]
        # backtracking - 2 decisions
        cur = [] # to track current combination
        def dfs(i, total):
            if total == n and len(cur) == k:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > n:
                return
            
            # decision 1: include candidate[i] and continue to include ith position
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            
            # decision 2: don't candidate[i] and don't use ith index ever
            cur.pop()
            dfs(i + 1, total)
            
        dfs(0, 0)
        return res