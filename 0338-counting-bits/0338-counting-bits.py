class Solution:
    def countBits(self, n: int) -> List[int]:
#         5 - 101
#         [0, 1, 1, 2, 1, 2]
        def countBits(i):
            count = 0
            while i:
                i = i & (i - 1)
                count += 1
            return count
        
        ans = [0] * (n + 1)
        for i in range(n + 1):
            # count number of 1 bits in i
            ans[i] = countBits(i)
        return ans