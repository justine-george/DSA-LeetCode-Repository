class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {(i, 1): 1 for i in ('a', 'e', 'i', 'o', 'u')}

        for i in range(2, n + 1):
            for j in ('a', 'e', 'i', 'o', 'u'):
                if j == 'a':
                    dp[('a', i)] = dp[('e', i - 1)] + dp[('i', i - 1)] + dp[('u', i - 1)]
                elif j == 'e':
                    dp[('e', i)] = dp[('a', i - 1)] + dp[('i', i - 1)]
                elif j == 'i':
                    dp[('i', i)] = dp[('e', i - 1)] + dp[('o', i - 1)]
                elif j == 'o':
                    dp[('o', i)] = dp[('i', i - 1)]
                else:
                    dp[('u', i)] = dp[('i', i - 1)] + dp[('o', i - 1)]

        return sum(dp[(i, n)] for i in ('a', 'e', 'i', 'o', 'u')) % (10 ** 9 + 7)