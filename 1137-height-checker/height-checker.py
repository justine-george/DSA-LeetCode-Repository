class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 if original != sorted else 0 for original, sorted in zip(heights, sorted(heights))])