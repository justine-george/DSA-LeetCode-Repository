class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            sum = 0
            while n:
                sum += (n % 10) ** 2
                n = n // 10
            return sum
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumOfSquares(n)
        return True
    
        # solution using floyd's cycle detection
        # fast, slow pointers always meet in case of a cycle
        
        slow, fast = n, sumOfSquares(n)
        while slow != fast:
            fast = sumOfSquares(fast)
            fast = sumOfSquares(fast)
            slow = sumOfSquares(slow)
        
        return True if fast == 1 else False