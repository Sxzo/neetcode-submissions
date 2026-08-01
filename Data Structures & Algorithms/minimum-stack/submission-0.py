class MinStack:
    # 3, 5, 2, 1
    # At every given length, the min is X
    def __init__(self):
        self.stack = []
        self.min_val_length = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        self.min_val_length[len(self.stack)] = min(val, self.min_val_length.get(len(self.stack) - 1, float('inf')))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_val_length[len(self.stack)]
        
