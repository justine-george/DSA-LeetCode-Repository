class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_to_walk = max(left) if left else float('-inf')
        right_to_walk = n - min(right) if right else float('-inf')

        return max(right_to_walk, left_to_walk)