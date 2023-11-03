class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symboldict = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in symboldict:
                top_elem = stack.pop() if stack else '#'
                if symboldict[c] != top_elem:
                    return False
            else:
                stack.append(c)
        return not stack