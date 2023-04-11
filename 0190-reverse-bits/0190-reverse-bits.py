class Solution:
    def reverseBits(self, n: int) -> int:
        res = [0] * 32
        i = 0
        while n and i < 32:
            res[i] = n & 1
            n = n >> 1
            i += 1
            
        return int("".join(str(r) for r in res), 2)