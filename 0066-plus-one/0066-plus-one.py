class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # numVal = int("".join(str(e) for e in digits))
        # numVal += 1
        # return [int(digit) for digit in str(numVal)]
    
        res = []
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + carry
            if i == (len(digits) - 1):
                sum += 1
            carry = sum // 10
            digits[i] = sum % 10
            
            if carry == 0:
                break
        if carry != 0:
            return [carry] + digits
        return digits