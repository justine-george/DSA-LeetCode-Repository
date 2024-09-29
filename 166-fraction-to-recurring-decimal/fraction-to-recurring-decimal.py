class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = ""
        if numerator * denominator < 0:
            res += '-'
        
        numerator = abs(numerator)
        denominator = abs(denominator)

        res += str(numerator // denominator)
        if numerator % denominator == 0:
            return res

        res += "."

        found_num_quotients = []
        while True:
            remainder = numerator % denominator

            if remainder == 0:
                for num_quotient in found_num_quotients:
                    res += str(num_quotient[1])
                return res

            numerator = remainder * 10
            new_quotient = numerator // denominator
            
            if [numerator, new_quotient] not in found_num_quotients:
                found_num_quotients.append([numerator, new_quotient])
            else:
                index_found = found_num_quotients.index([numerator, new_quotient])
                for num_quotient in found_num_quotients[:index_found]:
                    res += str(num_quotient[1])

                res += "("
                for num_quotient in found_num_quotients[index_found:]:
                    res += str(num_quotient[1])
                res += ")"
                return res