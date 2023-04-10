class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            sum = 0
            for digit in str(n):
                sum += int(digit) ** 2
            return sum
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumOfSquares(n)
        return True