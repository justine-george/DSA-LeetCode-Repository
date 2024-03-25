class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                val, idx = stack.pop()
                cur_height = val
                cur_width = i - idx
                max_area = max(max_area, cur_height * cur_width)
                start = idx
            
            stack.append((h, start))
        
        return max_area
