class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_palindrome(s, l, r):
            @lru_cache(None)
            def helper(l, r):
                if l >= r:
                    return True
                if s[l] != s[r]:
                    return False
                return helper(l + 1, r - 1)
            return helper(l, r)

        def dfs(i):
            if i == len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res