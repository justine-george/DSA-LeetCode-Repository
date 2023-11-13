class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            try:
                val = int(c)
                stack.append(val)
            except ValueError:
                second = stack.pop()
                first = stack.pop()
                stack.append(self.operate(first, second, c))
        
        return stack[0]

    def operate(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return int(a / b)