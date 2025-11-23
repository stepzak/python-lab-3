from collections import deque

from src.stack.abc import Stack


class QueueStack(Stack):

    def __init__(self):
        self.items = deque()
        self.min_items = deque()

    def min(self) -> int:
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.min_items[-1]

    def push(self, value):
        self.items.append(value)
        if len(self.min_items) == 0 or value <= self.min_items[-1]:
            self.min_items.append(value)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')

        val = self.items.pop()
        if val == self.min_items[-1]:
            self.min_items.pop()
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(0)
    print(stack, len(stack), stack.min(), stack.peek())
    print(stack.pop(), stack.min())
    stack.peek()

