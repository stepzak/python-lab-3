from typing import Callable, Any
from src.sort.base import T
from src.sort.factory import SortFactory


def sort(arr: list[T],
        key: Callable[[T], Any] | None = None,
        reverse: bool = False,
        cmp: Callable[[T, T], int] | None = None,
        *,
        algorithm: str = 'quick',
         **kwargs
) -> list[T]:
    algo = SortFactory.create_sorter(algorithm)
    return algo.sort(arr, key, reverse, cmp, **kwargs)

if __name__ == '__main__':
    print(sort([1, 5, 4, 2, 1], algorithm='bubble'))
    print(sort([1, 5, 4, 2, 1]))
    print(sort([-1, -5, -4, -2, -1, -5, -3], key = lambda x: -x ,algorithm='counting'))
    print(sort([52, 45, 456, 12, 1, 3, 2], algorithm='radix', base = 10))
    print(sort([52, 45, 456, 12, 1, 3, 2], algorithm='heap'))
    print(sort([0.5, 0.31, 0.1, 0.0001, 0.6, 0.25, 0.8], algorithm='bucket'))