class Solution:
    def calculate(self, s: str) -> int:
        cur, res = 0, 0
        sign = 1 # 1 for +, and -1 for -

        stack = []

        i = 0
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in '+-':
                res += sign * cur

                sign = 1 if char == '+' else -1
                cur = 0
            elif char == '(':
                stack.append((res, sign))
                # start a new calculate function
                sign = 1
                res = 0
            elif char == ')':
                # take care of edge case, similar to what we did when we see + or -
                res += sign * cur

                prev_res, sign = stack.pop()
                res = prev_res + res * sign
                cur = 0
        
        # take care of edge case, similar to what we did when we see + or -
        res += sign * cur

        return res






