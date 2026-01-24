class miniStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self,x):
            self.stack.append(x)
            if not self.minstack or x <= self.minstack[-1]:
                self.minstack.append(x)
    def pop(self):
         if not self.stack:
              return None
         val = self.stack.pop()
         if val ==  self.minstack[-1]:
            self.minstack.pop()
         return val
    def top(self):
         return self.stack[-1] if self.stack else None
    def getmin(self):
         return self.minstack[-1] if self.minstack else None
    
# --- Execution ---
obj = miniStack()  
obj.push(5)
obj.push(3)
obj.push(7)

print(obj.getmin()) 
obj.pop()           

print(obj.getmin()) 

obj.push(2)

print(obj.getmin()) 
