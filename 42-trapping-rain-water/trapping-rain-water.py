class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        total_water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                water_collected = max_left - height[left]
                if water_collected > 0:
                    total_water += water_collected
                max_left = max(height[left], max_left)
            else:
                right -= 1
                water_collected = max_right - height[right]
                if water_collected > 0:
                    total_water += water_collected
                max_right = max(height[right], max_right)

        return total_water