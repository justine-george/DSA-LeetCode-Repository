class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def dp(i, max_so_far, remain):
            if i == n:
                if remain == 0:
                    return 1
                
                return 0
            
            # when ith number is lteq max_so_far
            # search cost doesn't increase when ith number is lteq max_so_far
            # max_so_far choices
            ans = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD

            # when ith number is gt max_so_far
            # search cost increases with ith values gt max_so_far 
            for num in range(max_so_far + 1, m + 1):
                ans = (ans + dp(i + 1, num, remain - 1)) % MOD
                
            return ans
        
        MOD = 10 ** 9 + 7
        return dp(0, 0, k)