class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        121

        starting from 0:
            # single digit
            (if not 0) + starting from 1

            # 2 digit
            (if between 10 and 26 incl.) + starting from 2

        '''
        
        # # dp approach
        # # T: O(n), S: O(n)
        # n = len(s)
        # if n == 0 or s[0] == '0':
        #     return 0

        # dp = {n: 1}
        # for i in range(n - 1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]

        #     if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
        #         dp[i] += dp[i + 2]
        
        # return dp[0]

        # more efficient space, S:O(1)
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        
        next1, next2 = 1, 1 # base cases
        for i in range(n - 1, -1, -1):
            current = 0

            if s[i] != "0":
                current = next1
            
            if i + 1 < n and 10 <= int(s[i: i + 2]) <= 26:
                current += next2
            
            next2 = next1
            next1 = current
        
        return next1