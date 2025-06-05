class MyQueue:

    def __init__(self):
        self.add = []
        self.rem = []

    def push(self, x: int) -> None:
        self.add.append(x)

    def pop(self) -> int:
        while self.add:
            self.rem.append(self.add.pop())
        res = self.rem.pop()
        while self.rem:
            self.add.append(self.rem.pop())
        return res

    def peek(self) -> int:
        return self.add[0]

    def empty(self) -> bool:
        return False if self.add else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()