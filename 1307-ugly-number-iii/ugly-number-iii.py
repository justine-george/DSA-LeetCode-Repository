class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def hcf(a, b):
            if a == 0:
                return b
            return hcf(b % a, a)
        
        l, r = 1, 2e9
        lcm_ab = a * b // hcf(a, b)
        lcm_bc = b * c // hcf(b, c)
        lcm_ac = a * c // hcf(a, c)
        lcm_abc = lcm_ab * c // hcf(lcm_ab, c)
        
        while l < r:
            mid = l + (r - l) // 2
            count = mid // a + mid // b + mid // c - mid // lcm_ab - mid // lcm_bc - mid // lcm_ac + mid // lcm_abc
            # satisfies condition
            if count >= n:
                r = mid
            else:
                l = mid + 1

        return int(l)
