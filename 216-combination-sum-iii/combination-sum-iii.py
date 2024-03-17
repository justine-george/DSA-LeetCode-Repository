class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]

        res = []

        def dfs(pos, cur_arr, k_till_now, total):
            if k_till_now == k:
                if total == n:
                    res.append(cur_arr.copy())
                return
            
            for i in range(pos, len(candidates)):
                if total + candidates[i] > n:
                    break
                
                cur_arr.append(candidates[i])
                dfs(i + 1, cur_arr, k_till_now + 1, total + candidates[i])
                cur_arr.pop()

        dfs(0, [], 0, 0)
        return res