class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # find tallest to left
        tallest_to_left = [0] * n
        max_height = height[0]
        for i in range(1, n):
            if height[i - 1] > max_height:
                max_height = height[i - 1]
            tallest_to_left[i] = max_height
        
        # find tallest to right
        tallest_to_right = [0] * n
        max_height = height[-1]
        for i in range(n - 2, -1, -1):
            if height[i + 1] > max_height:
                max_height = height[i + 1]
            tallest_to_right[i] = max_height
        
        print(tallest_to_left)
        print(tallest_to_right)
        
        water_amount = 0
        for i in range(1, n - 1):
            water_amount += max(0, (min(tallest_to_right[i], tallest_to_left[i]) - height[i]))
        
        return water_amount
