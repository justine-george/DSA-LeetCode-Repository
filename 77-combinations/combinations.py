class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(cur_val, cur_arr, k_till_now):
            if k_till_now == k:
                res.append(cur_arr.copy())
                return
            
            for val in range(cur_val, n + 1):
                cur_arr.append(val)
                dfs(val + 1, cur_arr, k_till_now + 1)
                cur_arr.pop()


        dfs(1, [], 0)
        return res