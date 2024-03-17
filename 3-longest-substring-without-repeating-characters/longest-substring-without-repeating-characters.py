class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chosen = set()

        l = 0
        maxlen = 0
        for i, c in enumerate(s):
            while chosen and c in chosen:
                chosen.remove(s[l])
                l += 1
            
            chosen.add(c)
            maxlen = max(maxlen, i - l + 1)

        return maxlen

