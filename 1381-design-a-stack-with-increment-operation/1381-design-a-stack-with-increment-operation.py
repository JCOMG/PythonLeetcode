class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top < len(self.stack) - 1:
            self.top = self.top + 1
            self.stack[self.top] = x 

    def pop(self) -> int:
        if self.top != -1:
            value = self.stack[self.top]
            self.top = self.top - 1
            return value

        return -1

    #
    def increment(self, k: int, val: int) -> None:

        num_elements = min(k, self.top + 1)


        for i in range(num_elements):            
            self.stack[i] = self.stack[i] + val



