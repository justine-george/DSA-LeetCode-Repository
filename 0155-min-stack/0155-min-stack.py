class MinStack:

    def __init__(self):
        # (val, min_till_now)
        self.stack = []

    def push(self, val: int) -> None:
        # find minimum
        minim = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, minim))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()