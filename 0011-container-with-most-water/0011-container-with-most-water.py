class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = float('-inf')
        n = len(height)
        l, r = 0, n - 1
        while l < r:
            most_water = max(most_water, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return most_water