from src.stack.abc import Stack
from src.stack.linked_list_impl import LinkedListStack
from src.stack.list_impl import ListStack
from src.stack.queue_impl import QueueStack


class StackFactory:

    _stacks = {
        "linked_list": LinkedListStack,
        "list": ListStack,
        "queue": QueueStack
    }

    @classmethod
    def create(cls, stack_type: str) -> Stack:
        impl = cls._stacks.get(stack_type)
        if impl:
            return impl()

        raise ValueError(f"Unknown stack type: {stack_type}")

    @classmethod
    def get_available_types(cls) -> list[str]:
        return list(cls._stacks.keys())