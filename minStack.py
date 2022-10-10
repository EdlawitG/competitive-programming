class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_mins or val <= self.stack_mins[-1]:
            self.stack_mins.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.stack_mins[-1]:
            self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
