class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        res = 1
        l, r = 0, x // 2
        while l <= r:
            mid = l + ((r - l) // 2)
            int_sq = mid ** 2
            if int_sq == x:
                return mid
            elif int_sq < x:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        
        return res