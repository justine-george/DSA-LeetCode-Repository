class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        # first pass: mark invalid ')' and keep track of '(' positions
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        
        # second pass: remove unmatched '('
        while stack:
            s[stack.pop()] = ''
        
        return ''.join(s)