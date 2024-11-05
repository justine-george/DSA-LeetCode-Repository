class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)

        # first pass: mark invalid ')' and keep track of '(' positions
        for i, c in enumerate(s_list):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''
        
        # second pass: remove unmatched '('
        while stack:
            s_list[stack.pop()] = ''
        
        return ''.join(s_list)