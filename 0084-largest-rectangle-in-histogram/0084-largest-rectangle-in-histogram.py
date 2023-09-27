class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        # keep this monotonically non-decreasing
        # (start_index, height)
        stack = []

        # iterate through all heights, adding them into this monotonically non-decreasing stack
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                # pop
                top_index, top_height = stack.pop()
                # calculate area
                maxArea = max(maxArea, (i - top_index) * top_height)
                # update start
                start = top_index
            stack.append((start, height))
        
        # pop the heights remaining in the stack
        while stack:
            maxArea = max(maxArea, (n - stack[-1][0]) * stack[-1][1])
            stack.pop()
        
        return maxArea