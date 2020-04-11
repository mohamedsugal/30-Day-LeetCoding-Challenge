class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack: 
            self.stack.append((x, x))
        else: 
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        if self.stack: 
            self.stack.pop()

    def top(self) -> int:
        if self.stack: 
            return self.stack[-1][0]
        else: 
            return None

    def getMin(self) -> int:
        if self.stack: 
            return self.stack[-1][1]
        else: 
            return None 

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())    # should return -3 
obj.pop()
print(obj.top())       # should return 0
print(obj.getMin())    # should return -2