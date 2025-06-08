class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = []

    def next(self, val: int) -> float:
        self.arr.append(val)
        total = sum(self.arr[-self.size:])
        return total / min(len(self.arr), self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)