class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bitwise
        # https://youtu.be/cOFAmaMBVps?t=493
        ones, twos = 0, 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        return ones