class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
#         count = {}
#         res = 0
        
#         l = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             # if current window is not valid, reduce window from left
#             while (r - l + 1) - max(count.values()) > k:
#                 count[s[l]] -= 1
#                 l += 1
#             res = max(res, r - l + 1)
        
#         return res
    
        # More efficient
        count = {}
        res = 0
        
        l = 0
        maxCount = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxCount = max(maxCount, count[s[r]])
            # if current window is not valid, reduce window from left
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res