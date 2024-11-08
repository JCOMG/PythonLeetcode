class MyQueue:

    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x: int) -> None:
        while self.queue_1:  # 這一行的作用是迴圈地檢查 s1 是否有元素，只要 s1 不是空的，就會進入迴圈執行裡面的程式碼。
            self.queue_2.append(self.queue_1.pop())
        self.queue_1.append(x)

        while self.queue_2:
            self.queue_1.append(self.queue_2.pop())

    def pop(self) -> int:
        return self.queue_1.pop()

    def peek(self) -> int:
        return self.queue_1[-1]

    def empty(self) -> bool:
        return not self.queue_1

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()