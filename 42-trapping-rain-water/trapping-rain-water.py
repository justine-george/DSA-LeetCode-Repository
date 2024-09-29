class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        total_amount_water = 0

        while l < r:
            if max_l < max_r:
                l += 1
                amt = max_l - height[l]
                total_amount_water += amt if amt > 0 else 0
                max_l = max(height[l], max_l)
            else:
                r -= 1
                amt = max_r - height[r]
                total_amount_water += amt if amt > 0 else 0
                max_r = max(height[r], max_r)

        return total_amount_water