class Solution:
    def numberToWords(self, num: int) -> str:
        single = [""] + "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = ["", ""] + "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        
        def toWords(n):
            if n == 0:
                return ""
            if n // (10**9) > 0:
                return toWords(n // (10**9)) + "Billion " + toWords(n % (10**9))
            if n // (10**6) > 0:
                return toWords(n // (10**6)) + "Million " + toWords(n % (10**6))
            if n // 1000 > 0:
                return toWords(n // (10**3)) + "Thousand " + toWords(n % (10**3))
            if n // 100 > 0:
                return single[n // 100] + " " + "Hundred " + toWords(n % 100)
            if n > 19 and (n // 10) > 0:
                return tens[n // 10] + " " + toWords(n%10)
            return single[n] + " "
        
        if num == 0:
            return "Zero"
        
        return toWords(num).strip()
    

    # 1     231231231
    #   231     231231
    #   2   31     231231
    #   2   31     231  231