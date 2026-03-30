class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # update min at current spot
        # if min stack is empty, set to infinity
        top = self.min_stack[-1] if self.min_stack else float("inf")
        val = min(val, top)
        self.min_stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
