class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        val = ""
        for num in digits:
            val += str(num)
        numVal = int(val)
        numVal += 1
        return [int(digit) for digit in str(numVal)]