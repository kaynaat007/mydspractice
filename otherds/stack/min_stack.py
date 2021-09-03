class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) > 0:
            if self.min_stack[-1] >= x:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:

        return self.min_stack[-1]

s = MinStack()
s.push(-2)
s.push(0)
s.push(-3 )
print(s.getMin())
s.pop()
print(s.top())
print(s.getMin())


