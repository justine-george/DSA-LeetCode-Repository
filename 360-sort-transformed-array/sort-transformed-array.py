class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def get_val(x, a, b, c):
            return (a * x * x) + (b * x) + c
        
        return sorted([get_val(n, a, b, c) for n in nums])