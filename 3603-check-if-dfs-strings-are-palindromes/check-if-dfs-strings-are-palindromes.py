class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        N = len(parent)
        BASE = 31
        MOD = 37124508045065437
        orda = ord('a')

        # p[i] = (BASE ** i) % MOD
        p = [1] # BASE ** 0
        for _ in range(N):
            p.append((p[-1] * BASE) % MOD)
        
        # parent-child map
        e = collections.defaultdict(list)
        for i, par in enumerate(parent):
            if par != -1:
                e[par].append(i)
        
        ans = [None] * N

        @cache
        # this returns the string hash for the subtree going from
        # left to right, and also the size of the subtree
        def go_l2r(node):
            # current rolling hash
            current = 0
            # current nodes in this subtree
            totaln = 0

            for child in e[node]:
                h, num_n = go_l2r(child)
                current = current * p[num_n]
                current %= MOD
                current += h
                current %= MOD
                totaln += num_n
            
            current = (current * p[1]) + (ord(s[node]) - orda) + 1
            current %= MOD
            totaln += 1

            return (current, totaln)
        

        @cache
        # this returns the string hash for the subtree going from
        # right to left, and also the size of the subtree
        def go_r2l(node):
            # current rolling hash
            current = 0
            # current nodes in this subtree
            totaln = 0

            current = (current * p[1]) + (ord(s[node]) - orda) + 1
            current %= MOD
            totaln += 1

            for child in reversed(e[node]):
                h, num_n = go_r2l(child)
                current = current * p[num_n]
                current %= MOD
                current += h
                totaln += num_n
            
            current %= MOD
            return (current, totaln)


        def go(node):
            l2r = go_l2r(node) # go left to right
            r2l = go_r2l(node) # go right to left

            ans[node] = (l2r == r2l)

            for child in e[node]:
                go(child)
        
        go(0)
        return ans
