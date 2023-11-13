class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                stack.append(-stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack.pop()


    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     for c in tokens:
    #         try:
    #             val = int(c)
    #             stack.append(val)
    #         except ValueError:
    #             # pops from left to right, so first popped number is the second operand
    #             stack.append(self.operate(stack.pop(), stack.pop(), c))
        
    #     return stack.pop()

    # def operate(self, b, a, op):
    #     if op == '+':
    #         return a + b
    #     elif op == '-':
    #         return a - b
    #     elif op == '*':
    #         return a * b
    #     else:
    #         return int(a / b)