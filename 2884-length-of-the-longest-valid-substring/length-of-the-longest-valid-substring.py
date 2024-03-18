class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        invalid = set(forbidden)
        max_len = 0
        l = r_wall = len(word) - 1

        while l >= 0:
            for j in range(l, min(r_wall, l + 9) + 1):
                if word[l : j + 1] in invalid:
                    r_wall = j - 1
                    break
                    
            max_len = max(max_len, r_wall - l + 1)
            l -= 1
        
        return max_len