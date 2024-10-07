class Solution:
    def numberToWords(self, num: int) -> str:
        # 123000 -> one hundred twenty three thousand
        # 123 -> one hundred twenty three
        # 1,230,000->one million two hundred thirty thousand
        # 1,230->one thousand two hundred thirty

        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def toString(n):
            # 123, 120, 102, 012, 100
            res = []
            hundreds = n // 100
            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")
            last_two = n % 100
            if last_two >= 20:
                tens, ones = last_two // 10, last_two % 10
                res.append(tens_map[tens * 10])
                if ones:
                    res.append(ones_map[ones])
            elif last_two != 0:
                res.append(ones_map[last_two])

            return ' '.join(res)

        postfix = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        while num:
            digits = num % 1000

            s = toString(digits)
            if s:
                res.append(s + postfix[i])
            i += 1
            num = num // 1000

        res.reverse()
        return ' '.join(res)