class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [n for n in nums if n % 2 == 0]
        odd = [n for n in nums if n % 2 != 0]
        return even + odd