class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(cur_val, cur_arr, k_till_now, total):
            if k_till_now == k:
                if total == n:
                    res.append(cur_arr.copy())
                return
            
            for i in range(cur_val, 10):
                if total + i > n:
                    break
                
                cur_arr.append(i)
                dfs(i + 1, cur_arr, k_till_now + 1, total + i)
                cur_arr.pop()

        dfs(1, [], 0, 0)
        return res