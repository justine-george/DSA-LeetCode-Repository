class Solution:
    def splitString(self, s: str) -> bool:
        # 05 0043

        def dfs(prev, i):
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                cur = int(s[i:j + 1])
                if cur + 1 == prev and dfs(cur, j + 1):
                    return True

        for i in range(len(s) - 1):
            if dfs(int(s[:i + 1]), i + 1):
                return True
        return False