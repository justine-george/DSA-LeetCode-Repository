class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = 0
        while n > 0:
            bit += n % 2
            n = n // 2
        return bit