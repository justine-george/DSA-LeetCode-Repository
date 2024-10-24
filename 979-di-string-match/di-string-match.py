class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # N = len(s)
        # res = []
        # stack = []
        # for i in range(N + 1):
        #     stack.append(i)

        #     if i == N or s[i] == 'I':
        #         while stack:
        #             res.append(stack.pop())
        
        # return res

        l, r = 0, len(s)
        res = []
        for c in s + '.':
            if c == 'I':
                res.append(l)
                l += 1
            elif c == 'D':
                res.append(r)
                r -= 1
            else:
                res.append(l if s[-1] == 'I' else r)
        return res