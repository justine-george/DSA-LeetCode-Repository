class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        # backtracking - 2 decisions
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # decision 1: include candidate[i] and continue to include ith position
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            # decision 2: don't candidate[i] and don't use ith index ever
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res