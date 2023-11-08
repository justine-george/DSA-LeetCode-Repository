class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if fx == sx and fy == sy and t == 1:
            return False

        x_diff = abs(fx - sx)
        y_diff = abs(fy - sy)
        diag_dist = min(x_diff, y_diff)
        extra_dist = abs(x_diff - y_diff)

        return True if diag_dist + extra_dist <= t else False
