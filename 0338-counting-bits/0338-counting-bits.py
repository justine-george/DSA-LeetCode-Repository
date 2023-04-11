class Solution:
    def countBits(self, n: int) -> List[int]:
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
    
        # 0 0000 
        # 1 0001 - offset 1
        # 2 0010 - offset 2
        # 3 0011 - offset 2
        # 4 0100 - offset 4
        # 5 0101 - offset 4
        # 6 0110 - offset 4
        # 7 0111 - offset 4
        # 8 1000 - offset 8
        
        # T: O(n), S: O(1)
        dp = [0] * (n + 1)
        offset = 1 # stores highest power of 2
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
            
        return dp