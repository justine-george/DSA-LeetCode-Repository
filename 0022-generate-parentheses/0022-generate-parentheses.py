class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add '(' if open < n
        # only add ')' if closed < open
        # given path is valid iff open == closed == n
        
        stack = []
        res = []
        
        def backtrack(open = 0, closed = 0):
            # base case
            if open == closed == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
        
        backtrack()
        return res