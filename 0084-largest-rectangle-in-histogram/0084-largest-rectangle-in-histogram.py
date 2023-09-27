class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)

        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append((start, h))

        return res