class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        res = 0
        for i, original_h in enumerate(heights):
            if sorted_heights[i] != original_h:
                res += 1

        return res