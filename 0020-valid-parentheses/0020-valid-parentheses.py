class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        stack = []
        map = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in map:
                top = stack.pop() if stack else 'dummy'
                if top != map[c]:
                    return False
            else:
                stack.append(c)
        return not stack