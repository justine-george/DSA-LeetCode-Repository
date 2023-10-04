class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        max_water = 0
        while l < r:

            # max_water = max(max_water, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                max_water = max(max_water, (r - l) * height[l])
                l += 1
            else:
                max_water = max(max_water, (r - l) * height[r])
                r -= 1
        return max_water