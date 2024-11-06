class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for letter in map[digits[i]]:
                backtrack(i + 1, path + [letter])

        backtrack(0, [])
        return res