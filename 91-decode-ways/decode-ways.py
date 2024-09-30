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
        '''
        Method to calculate the number of ways to decode a given encoded string 's'.

        Args:
        - s (str): The encoded string containing digits

        Returns:
        - int: The number of possible decoding ways.        
        '''

        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        
        dp = {n: 1} # base case: one way to decode an empty string
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # single digit decode
                dp[i] = dp[i + 1]
            
            # double digit decode
            if i + 1 < n and 10 <= int(s[i: i + 2]) <= 26:
                dp[i] += dp[i + 2]
        
        # returns number of ways to decode starting from 0th index.
        return dp[0]