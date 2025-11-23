from abc import ABC, abstractmethod
from typing import Any


class Stack(ABC):

    items: Any
    min_items: Any

    @abstractmethod
    def push(self, value: int) -> None:
        """Push item to stack."""

    @abstractmethod
    def pop(self) -> int:
        """Pop item from stack."""

    @abstractmethod
    def peek(self) -> int:
        """Peek item from stack."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if stack is empty."""

    @abstractmethod
    def min(self) -> int:
        """Minimum item from stack."""

    @abstractmethod
    def __len__(self) -> int:
        """Number of items in stack."""

    def __repr__(self) -> str:
        return f"Stack(items={self.items}, min={self.min() if self.min_items else 'None'})"