class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        op = '+'
        stack = []

        def helper(cur, op):
            if op == '+':
                stack.append(cur)
            elif op == '-':
                stack.append(-cur)
            elif op == '*':
                stack.append(stack.pop() * cur)
            elif op == '/':
                stack.append(int(stack.pop() / cur))
        
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char == '(':
                stack.append(op)
                cur = 0
                op = '+'
            elif char in '+-*/)':
                helper(cur, op)
                if char == ')':
                    cur = 0
                    while isinstance(stack[-1], int):
                        cur += stack.pop()
                    op = stack.pop()
                    helper(cur, op)
                cur = 0
                op = char
        
        helper(cur, op)
        return sum(stack)
