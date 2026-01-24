class queue:
    def __init__(self):
        self.outstack = []
        self.instack = []
    def push(self,x):
        self.instack.append(x)
    def _move(self):
        while self.instack:
            self.outstack.append(self.instack.pop())
    def pop(self):
        if not self.outstack:
            self._move()
        return self.outstack.pop()
    
obj = queue()

obj.push(10)
obj.push(45)
obj.push(7)
obj.push(1)

print(obj.pop())