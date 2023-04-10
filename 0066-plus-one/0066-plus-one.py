class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numVal = int("".join(str(e) for e in digits))
        numVal += 1
        return [int(digit) for digit in str(numVal)]