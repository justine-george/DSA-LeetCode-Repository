class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        path = []

        def dfs(i):
            if i == len(s):
                res.append(path[:])
                return
            
            for j in range(i, len(s)):
                if isPal(i, j):
                    path.append(s[i:j+1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return res