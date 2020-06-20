class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:        
        self.stack.append(x)
       
    def pop(self) -> None:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        
    def getMin(self) -> int: 
        if len(self.stack)==0:
            return []
        return min(self.stack)
