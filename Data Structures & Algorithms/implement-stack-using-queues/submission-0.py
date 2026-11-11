class MyQueue:
    def __init__(self):
        self.q = deque()
    
    def push(self, x: int) -> None:
        self.q.append(x)
    
    def pop(self) -> int:
        return self.q.popleft()
    
    def peek(self) -> int:
        return self.q[0]
    
    def size(self) -> int:
        return len(self.q)
    
    def empty(self) -> bool:
        return not self.q

class MyStack:

    def __init__(self):
        self.main = MyQueue()

    def push(self, x: int) -> None:
        self.main.push(x)

    def pop(self) -> int:
        temp_q = MyQueue()

        while self.main.size() > 1:
            temp_q.push(self.main.pop())
        
        res = self.main.pop()
        self.main = temp_q

        return res

    def top(self) -> int:
        res = self.pop()
        self.push(res)

        return res

    def empty(self) -> bool:
        return self.main.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()