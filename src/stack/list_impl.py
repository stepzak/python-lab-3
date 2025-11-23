from src.stack.abc import Stack

class ListStack(Stack):
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, x: int) -> None:
        self.items.append(x)
        if not self.min_items or x <= self.min_items[-1]:
            self.min_items.append(x)

    def is_empty(self) -> bool:
        return not self.items

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('stack is empty')
        ret = self.items.pop()
        if ret == self.min_items[-1]:
            self.min_items.pop()
        return ret

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('stack is empty')
        return self.items[-1]

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def min(self) -> int:
        if not self.min_items:
            raise IndexError('min from empty stack')
        return self.min_items[-1]

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(0)
    print(stack, len(stack), stack.min(), stack.peek())
    print(stack.pop(), stack.min())
    stack.peek()