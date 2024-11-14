class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(path, pathSum):
            if pathSum == target:
                res.add(tuple(sorted(path[:])))
                return

            if pathSum > target:
                return

            for c in candidates:
                dfs(path + [c], pathSum + c)

        dfs([], 0)
        return list(res)