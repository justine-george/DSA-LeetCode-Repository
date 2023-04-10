class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            sum = 0
            while n:
                d = n % 10
                d = d ** 2
                sum += d
                n = n // 10
            return sum
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumOfSquares(n)
        return True