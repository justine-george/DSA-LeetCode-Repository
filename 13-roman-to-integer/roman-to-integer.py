class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = roman_map[s[len(s) - 1]]
        for i in range(len(s) - 2, -1, -1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                res -= roman_map[s[i]]
            else:
                res += roman_map[s[i]]
        return res

        # roman_map = {
        #     "I": 1,
        #     "IV": 4,
        #     "V": 5,
        #     "IX": 9,
        #     "X": 10,
        #     "XL": 40,
        #     "L": 50,
        #     "XC": 90,
        #     "C": 100,
        #     "CD": 400,
        #     "D": 500,
        #     "CM": 900,
        #     "M": 1000
        # }
        # i = 0
        # res = 0
        # while i < len(s):
        #     if i + 1 < len(s) and s[i:i+2] in roman_map:
        #         res += roman_map[s[i:i+2]]
        #         i += 2
        #     else:
        #         res += roman_map[s[i]]
        #         i += 1
        # return res