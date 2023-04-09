class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         res = []
#         cur = []
#         candidates = [i for i in range(1, 10)]
#         # backtracking
#         def dfs(i, total, depth):
#             if depth == k:
#                 if total == n:
#                     res.append(cur.copy())
#                 return
            
#             for j in range(i, len(candidates)):
#                 if total + candidates[j] > n:
#                     break
#                 cur.append(candidates[j])
#                 dfs(j + 1, total + candidates[j], depth + 1)
#                 cur.pop()
        
#         dfs(0, 0, 0)
#         return res
    
        res = []
        candidates = [i for i in range(1, 10)]
        # backtracking - 2 decisions
        cur = [] # to track current combination
        def dfs(i, total, depth):
            # if depth == k:
            if total == n:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > n:
                return
            
            # decision 1: include candidate[i] and continue to include ith position
            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i], depth + 1)
            
            # decision 2: don't candidate[i] and don't use ith index ever
            cur.pop()
            dfs(i + 1, total, depth + 1)
            
        dfs(0, 0, 0)
        result = []
        for r in res:
            if len(r) == k:
                result.append(r)
        return result