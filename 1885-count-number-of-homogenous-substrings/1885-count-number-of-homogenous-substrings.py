class Solution:
    def countHomogenous(self, s: str) -> int:
        # 1 1
        # 2 3
        # 3 6
        # 4 10
        # 5 15
        def getSumTillN(n):
            return (n * (n + 1)) // 2

        # {n_at_a_time: count}
        map = defaultdict(int)
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and s[i] == s[start]:
                i += 1
            n_at_a_time = i - start
            map[n_at_a_time] += 1
        
        res = 0
        for n_at_a_time in map:
            res += getSumTillN(n_at_a_time) * map[n_at_a_time]
            res %= (10 ** 9 + 7)
        
        return res