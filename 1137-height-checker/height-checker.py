class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 if before != after else 0 for before, after in zip(heights, sorted(heights))])