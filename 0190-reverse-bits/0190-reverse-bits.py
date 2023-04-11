class Solution:
    def reverseBits(self, n: int) -> int:
        # res = [0] * 32
        # i = 0
        # while n and i < 32:
        #     res[i] = n & 1
        #     n = n >> 1
        #     i += 1
        # return int("".join(str(r) for r in res), 2)

        # S: O(1) approach
        res = 0
        for i in  range(32):
            # start from rightmost bit, and work towards left
            bit = (n >> i) & 1
            
            # start appending to left most position, work towards right
            res = res | (bit << (31 - i))
        return res