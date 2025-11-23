from src.stack.abc import Stack


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __eq__(self, other: "Node") -> bool:
        return self.value == other.value and self.next == other.next

    def __str__(self):
        ret = []
        head = self
        while head:
            ret.append(self.next.value)
            head = head.next

        return str(ret[::-1])

class LinkedListStack(Stack):
    def __init__(self):
        self.items: Node | None = None
        self.min_items: Node | None = None
        self.size = 0

    def push(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("stack only supports floats and ints")
        new_node = Node(value, self.items)
        self.items = new_node
        self.size += 1
        if self.min_items is None or self.min_items.value >= value:
            new_min_node = Node(value, self.min_items)
            self.min_items = new_min_node

    def is_empty(self) -> bool:
        return not self.items

    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        val = self.items.value
        self.items = self.items.next
        self.size -= 1
        if val == self.min_items.value:
            self.min_items = self.min_items.next
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        return self.items.value

    def __len__(self) -> int:
        return self.size

    def min(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        return self.min_items.value

    def __str__(self):
        elements = []
        current = self.items
        while current:
            elements.append(current.value)
            current = current.next
        return str(elements[::-1])

    def __repr__(self):
        return f'Stack(items={self.items}, min_items={self.min_items})'

if __name__ == "__main__":
    stack = LinkedListStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(0)
    print(stack, len(stack), stack.min(), stack.peek())
    print(stack.pop(), stack.min())
    stack.peek()
