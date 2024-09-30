class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        total_water = 0
        while l < r:
            if max_left < max_right:
                l += 1
                water_collected = max_left - height[l]
                if water_collected > 0:
                    total_water += water_collected
                max_left = max(max_left, height[l])
            else:
                r -= 1
                water_collected = max_right - height[r]
                if water_collected > 0:
                    total_water += water_collected
                max_right = max(max_right, height[r])

        return total_water