class Solution:
    def numDecodings(self, s: str) -> int:
        # 121
        # ""
        # take one "1" (any number x 1<=x<=9 can be taken)
        #     take one "2"
        #         take one "1" end
        #     take two "21" end
        # take two "12" (any number x 1<=x<=26 can be taken)
        #     take one "1" end
        
        # n = len(s)
        # if n == 0 or s[0] == '0':
        #     return 0

        # total = 0
        # def count_decodings_from(index, s):
        #     nonlocal total
        #     if index == n:
        #         total += 1
        #         return
            
        #     if index < n and 0 < int(s[index]) < 10:
        #         count_decodings_from(index + 1, s)
            
        #     if index + 1 < n and 9 < int(s[index:index+2]) <= 26:
        #         count_decodings_from(index + 2, s)

        #     return

        # count_decodings_from(0, s)
        # return total

        # dp - more efficient
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if 0 < int(s[i-1:i]) < 10:
                dp[i] += dp[i - 1]
            if 9 < int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
