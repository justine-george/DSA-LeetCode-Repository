class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start):
            if start == len(s):
                res.append(part[:])
                return
            for i in range(start, len(s)):
                if is_palindrome(s, start, i):
                    part.append(s[start:i+1])
                    dfs(i + 1)
                    part.pop()

        dfs(0)
        return res