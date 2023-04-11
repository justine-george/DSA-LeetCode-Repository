class Solution:
    def reverseBits(self, n: int) -> int:
        res = []
        while n:
            res.append(n % 2)
            n = n >> 1
        
        rem = 32 - len(res)
        for i in range(rem):
            res.append(0)
            
        return int("".join(str(r) for r in res), 2)