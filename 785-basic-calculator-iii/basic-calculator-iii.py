class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        op = '+'

        def helper(op, cur):
            match op:
                case '+':
                    stack.append(cur)
                case '-':
                    stack.append(-cur)
                case '*':
                    stack.append(stack.pop() * cur)
                case '/':
                    stack.append(int(stack.pop() / cur))
                case _:
                    print(') case')


        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char == '(':
                stack.append(op)
                cur = 0
                op = '+'
            elif char in '+-*/)':
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