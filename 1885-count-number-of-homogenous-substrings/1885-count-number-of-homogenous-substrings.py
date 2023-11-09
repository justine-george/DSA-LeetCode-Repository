class Solution:
    def countHomogenous(self, s: str) -> int:
        def getSumTillN(n):
            return (n * (n + 1)) // 2
        i = 0
        res = 0
        while i < len(s):
            start = i
            while i < len(s) and s[i] == s[start]:
                i += 1
            n_at_a_time = i - start
            res += getSumTillN(n_at_a_time)
        return res % (10 ** 9 + 7)