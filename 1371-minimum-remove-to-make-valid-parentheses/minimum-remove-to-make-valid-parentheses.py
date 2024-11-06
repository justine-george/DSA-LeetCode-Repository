class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)

        for i, c in enumerate(s_list):
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''
            elif c == '(':
                stack.append(i)
        
        while stack:
            s_list[stack.pop()] = ''
        
        return ''.join(s_list)