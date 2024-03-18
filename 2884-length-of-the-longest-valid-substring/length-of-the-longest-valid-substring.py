class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        invalid = set(forbidden)
        max_len = 0

        i = r_wall = len(word) - 1
        while i >= 0:
            for j in range(i, min(r_wall, i + 9) + 1):
                if word[i:j + 1] in invalid:
                    r_wall = j - 1
                    break
            max_len = max(max_len, r_wall - i + 1)
            i -= 1
        
        return max_len