class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        stack = []
        map = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            # if it is opening, add
            if c in map:
                stack.append(c)
            # if it is closing, check:
            #   1. closing to an empty stack is False
            #   2. map[stack.pop()] this should be same as the incoming closing
            elif not stack or c != map[stack.pop()]:
                return False
        return not stack