class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        res = []
        stack = []
        for i in range(N + 1):
            stack.append(i + 1)

            if i == N or pattern[i] == 'I':
                while stack:
                    res.append(str(stack.pop()))
        
        return "".join(res)
        
        # N = len(pattern)
        # for t in permutations(range(1, N + 2)):
        #     for i in range(N):
        #         if t[i] > t[i + 1]:
        #             if pattern[i] == "I":
        #                 break
        #         else:
        #             if pattern[i] == "D":
        #                 break
        #     else:
        #         return "".join([str(n) for n in t])