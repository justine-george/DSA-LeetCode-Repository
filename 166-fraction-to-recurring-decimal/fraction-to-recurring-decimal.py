class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if numerator * denominator < 0:
            res.append('-')
        
        numerator = abs(numerator)
        denominator = abs(denominator)

        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(res)

        res.append('.')

        remainder_map = {}
        while True:
            if remainder in remainder_map:
                res.insert(remainder_map[remainder], '(')
                res.append(')')
                break

            remainder_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

            if remainder == 0:
                break
        
        return ''.join(res)