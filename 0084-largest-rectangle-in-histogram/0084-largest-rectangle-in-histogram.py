class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        # add a dummy height with height 0 to the end
        heights.append(0)

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
        
        # # pop the heights remaining in the stack
        # while stack:
        #     top_index, top_height = stack.pop()
        #     maxArea = max(maxArea, (n - top_index) * top_height)
        
        return maxArea