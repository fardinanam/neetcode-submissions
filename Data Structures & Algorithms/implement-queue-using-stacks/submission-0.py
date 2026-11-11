class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = deque()

        while len(self.stack) > 1:
            temp.append(self.stack.pop())
        
        res = self.stack.pop()
        
        while temp:
            self.stack.append(temp.pop())

        return res

    def peek(self) -> int:
        temp = deque()

        while len(self.stack) > 1:
            temp.append(self.stack.pop())
        
        res = self.stack[-1]

        while temp:
            self.stack.append(temp.pop())

        return res
        

    def empty(self) -> bool:
        return not self.stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()