class Solution:
    def countBits(self, n: int) -> List[int]:
#         5 - 101
#         [0, 1, 1, 2, 1, 2]
#         def countBits(i):
#             count = 0
#             while i:
#                 # zeroing out the least significant nonzero bit
#                 i = i & (i - 1) 
#                 count += 1
#             return count
        
#         # T: O(nlogn), S: O(1)
#         ans = [0] * (n + 1)
#         for i in range(n + 1):
#             # count number of 1 bits in i
#             ans[i] = countBits(i)
#         return ans
    
        # T: O(n), S: O(1)
        dp = [0] * (n + 1)
        offset = 1 # stores highest power of 2
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
            
        return dp