class MinStack:

    def __init__(self):
        # either insert tuples into one stack or use separate minstack, push and pop in sync
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1] if self.stack else val)))
        
    def pop(self) -> None:
        self.stack.pop()
        
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