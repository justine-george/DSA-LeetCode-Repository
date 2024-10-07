class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n = -n

        # T: O(logn)
        # S: O(1)
        res = 1
        while n != 0:
            # power is an odd number
            if n % 2 == 1:
                res *= x
                n -= 1
            
            # now power is even
            # x**n = (x**2)**(n/2)
            x *= x
            n //= 2

        return res