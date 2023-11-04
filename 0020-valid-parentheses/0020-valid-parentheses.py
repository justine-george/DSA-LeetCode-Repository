class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for c in s:
            # if c is closing
            if c not in map:
                top = stack.pop() if stack else '#'
                if top not in map or map[top] != c:
                    return False
            # if c is opening
            else:
                stack.append(c)
        
        return not stack