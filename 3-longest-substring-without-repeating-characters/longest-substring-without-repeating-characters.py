class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chosen = set()
        l = 0
        maxlen = 0

        for r, c in enumerate(s):
            while c in chosen:
                chosen.remove(s[l])
                l += 1
            
            chosen.add(c)
            maxlen = max(maxlen, r - l + 1)

        return maxlen

