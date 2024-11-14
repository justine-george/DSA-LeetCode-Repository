class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, pathSum):
            if pathSum == target:
                res.append(path[:])
                return

            if i == len(candidates) or pathSum > target:
                return

            dfs(i + 1, path, pathSum)

            dfs(i, path + [candidates[i]], pathSum + candidates[i])

        dfs(0, [], 0)
        return res