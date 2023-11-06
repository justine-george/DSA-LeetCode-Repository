class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        # self.minMap = {0: float('inf')}
        # self.min = float('inf')
        # self.size = 0
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
        
        # self.stack.append(val)
        # self.size += 1
        # self.min = min(self.min, val)
        # self.minMap[self.size] = self.min
        # print(f"{self.stack}: min: {self.min}")

    def pop(self) -> None:
        self.stack.pop()
        # self.size -= 1
        # self.min = self.minMap[self.size]
        # print(f"{self.stack}: min: {self.min}")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()