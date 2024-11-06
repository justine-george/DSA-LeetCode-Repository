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
            
            current_digit = digits[i]
            for letter in map[current_digit]:
                path.append(letter)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res