class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        op = '+'
        stack = []

        def helper(op, cur):
            if op == '+':
                stack.append(cur)
            elif op == '-':
                stack.append(-cur)

        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in '(':
                stack.append(op)

                cur = 0
                op = '+'
            elif char in '+-)':
                helper(op, cur)
                if char == ')':
                    cur = 0
                    while isinstance(stack[-1], int):
                        cur += stack.pop()
                    op = stack.pop()
                    helper(op, cur)

                cur = 0
                op = char
        
        helper(op, cur)

        return sum(stack)


        # cur, res = 0, 0
        # sign = 1 # 1 for +, and -1 for -

        # stack = []

        # i = 0
        # for char in s:
        #     if char.isdigit():
        #         cur = cur * 10 + int(char)
        #     elif char in '+-':
        #         res += sign * cur

        #         sign = 1 if char == '+' else -1
        #         cur = 0
        #     elif char == '(':
        #         stack.append((res, sign))
        #         # start a new calculate function
        #         sign = 1
        #         res = 0
        #     elif char == ')':
        #         # take care of edge case, similar to what we did when we see + or -
        #         res += sign * cur

        #         prev_res, sign = stack.pop()
        #         res = prev_res + res * sign
        #         cur = 0
        
        # # take care of edge case, similar to what we did when we see + or -
        # res += sign * cur

        # return res


