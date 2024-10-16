class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_int_map[s[i]] < roman_int_map[s[i + 1]]:
                res -= roman_int_map[s[i]]
            else:
                res += roman_int_map[s[i]]
        
        return res