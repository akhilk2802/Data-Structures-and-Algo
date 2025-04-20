class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if minStack is empty *or* val is <= current min, push it
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        

    def pop(self) -> None:
        if self.isEmpty():
            return None
        value = self.stack.pop()
        if self.minStack and self.minStack[-1] == value:
            self.minStack.pop()
        return value
        

    def top(self) -> int:
        if self.isEmpty():
            return None
        value = self.stack[-1]
        return value
        

    def getMin(self) -> int:
        if self.isEmpty():
            return None
        value = self.minStack[-1]
        return value
    
    def isEmpty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()