class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(cur_arr, pos, total):
            if total == target:
                res.append(cur_arr.copy())
                return
            if total > target:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue

                cur_arr.append(candidates[i])
                dfs(cur_arr, i + 1, total + candidates[i])
                cur_arr.pop()

                prev = candidates[i]

        dfs([], 0, 0)
        return res