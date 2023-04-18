class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for a, b in zip_longest(word1, word2):
            if a:
                res += a
            if b:
                res += b
        return res