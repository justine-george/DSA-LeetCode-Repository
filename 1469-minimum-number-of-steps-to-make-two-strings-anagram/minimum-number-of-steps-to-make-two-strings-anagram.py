class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return sum((s_counter - t_counter).values())

        res = 0
        for char in t_counter:
            if char not in s_counter:
                res += t_counter[char]
            else:
                diff = t_counter[char] - s_counter[char]
                if diff > 0:
                    res += diff
        return res

        '''
        a: 1
        b: 2

        a: 2
        b: 1

        differ: a:-1,b:1
        plus: 1
        neg: 1
        res = 1
----------------------
        c: 1
        d: 1
        e: 3      
        l: 1
        o: 1
        t: 1

        a: 1
        c: 2
        e: 1
        i: 1
        p: 1
        r: 1
        t: 1

        differ: a:1, c:1, d:-1, e:-2, i:1, l:-1, o:-1, p:1, r:1

        plus: 5
        neg: 5
        res = 5
        '''