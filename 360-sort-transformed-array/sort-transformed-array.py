class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def get_val(x, a, b, c):
            return (a * x * x) + (b * x) + c
        
        res = []
        l, r = 0, len(nums) - 1

        if a < 0:
            # downward parabola, we put smaller edge element first
            while l <= r:
                left_val = get_val(nums[l], a, b, c)
                right_val = get_val(nums[r], a, b, c)
                if left_val < right_val:
                    res.append(left_val)
                    l += 1
                else:
                    res.append(right_val)
                    r -= 1
        else:
            # upward parabola/straight line, we put bigger edge element first
            while l <= r:
                left_val = get_val(nums[l], a, b, c)
                right_val = get_val(nums[r], a, b, c)
                if left_val > right_val:
                    res.append(left_val)
                    l += 1
                else:
                    res.append(right_val)
                    r -= 1
            res.reverse()

        return res