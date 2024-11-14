class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, path, pathSum):
            if pathSum == target:
                res.append(path[:])
                return
            
            if i == len(candidates) or pathSum > target:
                return
            
            dfs(i + 1, path + [candidates[i]], pathSum + candidates[i])

            # skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, path, pathSum)

        
        dfs(0, [], 0)
        return res