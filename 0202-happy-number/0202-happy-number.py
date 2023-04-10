class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            return sum(int(digit) ** 2 for digit in str(n))
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumOfSquares(n)
        return True