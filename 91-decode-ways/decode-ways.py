class Solution:
    def numDecodings(self, s: str) -> int:
        # if len(s) == 0 or s[0] == "0":
        #     return 0

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] += dp[i + 1]
            if i + 2 <= len(s) and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]
        
        return dp[0]