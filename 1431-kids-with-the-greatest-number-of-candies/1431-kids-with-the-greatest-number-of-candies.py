class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        val = max(candies) - extraCandies
        return [True if c >= val else False for c in candies]