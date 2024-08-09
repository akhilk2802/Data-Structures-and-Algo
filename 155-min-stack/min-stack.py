class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.isEmpty():
            return None
        self.stack.pop()

    def top(self) -> int:
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack) == 0


    def getMin(self) -> int:
        if self.isEmpty():
            return None
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()