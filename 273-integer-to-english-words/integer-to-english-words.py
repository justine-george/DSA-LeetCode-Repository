class Solution:
    def numberToWords(self, num: int) -> str:
        # 123000 -> one hundred twenty three thousand
        # 123 -> one hundred twenty three
        # 1,230,000->one million two hundred thirty thousand
        # 1,230->one thousand two hundred thirty

        single = [""] + "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = ["", ""] + "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()

        def toString(n):
            if n == 0:
                return ""
            if n // 10**9:
                return toString(n // 10**9) + " Billion " + toString(n % 10**9)
            if n // 10**6:
                return toString(n // 10**6) + " Million " + toString(n % 10**6)
            if n // 10**3:
                return toString(n // 10**3) + " Thousand " + toString(n % 10**3)
            
            if n // 100:
                return (toString(n // 100) + " Hundred " + toString(n % 100)).strip()
            if n > 19:
                return (tens[n // 10] + " " + toString(n % 10)).strip()
            
            return single[n]

        if num == 0:
            return "Zero"
        
        return toString(num).strip()