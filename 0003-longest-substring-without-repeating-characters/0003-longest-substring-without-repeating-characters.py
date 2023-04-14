class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window with string slicing
        # curset = ""
        # maxLen = 0
        # for i in range(len(s)):
        #     if s[i] in curset:
        #         while curset[0] != s[i]:
        #             curset = curset[1:]
        #         while curset and curset[0] == s[i]:
        #             curset = curset[1:]
        #     curset += s[i]
        #     maxLen = max(maxLen, len(curset))
        # return maxLen
    
    
        # sliding window with set
        curset = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in curset:
                curset.remove(s[l])
                l += 1
            curset.add(s[r])
            maxLen = max(maxLen, len(curset))
        return maxLen