class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curset = ""
        maxLen = 0
        for i in range(len(s)):
            if s[i] in curset:
                while curset[0] != s[i]:
                    curset = curset[1:]
                while curset and curset[0] == s[i]:
                    curset = curset[1:]
            curset += s[i]
            # print(f"curset: {curset}")
            maxLen = max(maxLen, len(curset))
        return maxLen
    
    # curset = abc
    # maxLen = 3