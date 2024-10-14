class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # euclidean algorithm to find GCD
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)
        
        l, r = 1, 2e9
        ab = a * b // gcd(a, b)
        bc = b * c // gcd(b, c)
        ac = a * c // gcd(a, c)
        abc = a * bc // gcd(a, bc)
        
        while l < r:
            mid = l + (r - l) // 2
            count = mid // a + mid // b + mid // c - mid // ab - mid // bc - mid // ac + mid // abc
            if count >= n: # f(x) >= n, we have to find first x that satisfies this
                r = mid
            else:
                l = mid + 1
        return int(l)