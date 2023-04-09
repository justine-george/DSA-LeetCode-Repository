class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cur = []
        candidates = [i for i in range(1, 10)]
        # backtracking
        def dfs(i, total, depth):
            if total == n and depth == k:
                res.append(cur.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > n:
                    break
                cur.append(candidates[j])
                dfs(j + 1, total + candidates[j], depth + 1)
                cur.pop()
        
        dfs(0, 0, 0)
        return res