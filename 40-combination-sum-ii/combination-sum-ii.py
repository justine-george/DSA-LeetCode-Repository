class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(cur_arr, pos, total):
            if total == target:
                res.append(cur_arr.copy())
                return
            
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                cur_arr.append(candidates[i])
                dfs(cur_arr, i + 1, total + candidates[i])
                cur_arr.pop()

        dfs([], 0, 0)
        return res