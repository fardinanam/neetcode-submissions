class MyCircularQueue:
    def __init__(self, k: int):
        self.store = [0] * k
        self.head = self.tail = 0
        self.empty = True

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.empty = False
        self.store[self.tail] = value
        self.tail = (self.tail + 1) % len(self.store)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % len(self.store)
        if self.head == self.tail:
            self.empty = True

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.store[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.store[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.empty

    def isFull(self) -> bool:
        return self.head == self.tail and not self.isEmpty()


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
