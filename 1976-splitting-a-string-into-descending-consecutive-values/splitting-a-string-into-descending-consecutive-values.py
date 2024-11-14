class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(prev, i):
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                cur = int(s[i:j+1])
                if cur == prev - 1 and dfs(cur, j + 1):
                    return True

            return False
        
        for i in range(len(s) - 1):
            cur = int(s[:i + 1])
            if dfs(cur, i + 1):
                return True
        
        return False