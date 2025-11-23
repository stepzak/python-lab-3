import pytest
from src.stack.linked_list_impl import Node
from src.stack.factory import StackFactory
from collections import deque

@pytest.mark.parametrize(
    "stack_type,to_push,expected",
    [
        ("linked_list", [1, 2, 3], Node(value=3, next = Node(2, next = Node(1)))),
        ("list", [1, 2, 3], [1, 2, 3]),
        ("queue", [1, 2, 3], deque([1, 2, 3])),
    ]
)
def test_push(stack_type, to_push, expected):
    stack = StackFactory().create(stack_type)
    for item in to_push:
        stack.push(item)
    assert stack.items == expected

@pytest.mark.parametrize(
    "stack_type,to_push,expected",
[
        ("linked_list", [1, 2, 3], Node(value=2, next = Node(1))),
        ("list", [1, 2, 3], [1, 2]),
        ("queue", [1, 2, 3], deque([1, 2])),
    ]
)
def test_pop(stack_type, to_push, expected):
    stack = StackFactory().create(stack_type)
    for item in to_push:
        stack.push(item)
    val = stack.pop()
    assert stack.items == expected
    assert val == to_push[-1]


@pytest.mark.parametrize(
    "stack_type,to_push,expected",
[
        ("linked_list", [1, 2, 3], 3),
        ("list", [1, 2, 3], 3),
        ("queue", [1, 2, 3], 3),
    ]
)
def test_peek(stack_type, to_push, expected):
    stack = StackFactory().create(stack_type)
    for item in to_push:
        stack.push(item)
    assert stack.peek() == expected

@pytest.mark.parametrize(
    "stack_type,to_push,expected",
[
        ("linked_list", [1, 2, 3], 1),
        ("list", [1, 2, 3], 1),
        ("queue", [1, 2, 3], 1),
    ]
)
def test_min(stack_type, to_push, expected):
    stack = StackFactory().create(stack_type)
    for item in to_push:
        stack.push(item)
    assert stack.min() == expected

@pytest.mark.parametrize(
    "stack_type,to_push,expected",
[
        ("linked_list", [3, 2, 1], 2),
        ("list", [3, 2, 1], 2),
        ("queue", [3, 2, 1], 2),
    ]
)
def test_pop_min(stack_type, to_push, expected):
    stack = StackFactory().create(stack_type)
    for item in to_push:
        stack.push(item)
    stack.pop()
    assert stack.min() == expected