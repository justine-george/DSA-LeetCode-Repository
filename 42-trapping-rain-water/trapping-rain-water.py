class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        tallest_to_left = [0] * n
        tallest_till_now = height[0]
        for i in range(1, n):
            tallest_till_now = max(tallest_till_now, height[i - 1])
            tallest_to_left[i] = tallest_till_now
        
        tallest_to_right = [0] * n
        tallest_till_now = height[n - 1]
        for i in range(n - 2, -1, -1):
            tallest_till_now = max(tallest_till_now, height[i + 1])
            tallest_to_right[i] = tallest_till_now
        
        res = 0
        for i in range(n):
            amount_at_i = min(tallest_to_left[i], tallest_to_right[i]) - height[i]
            res += (amount_at_i if amount_at_i > 0 else 0)

        return res