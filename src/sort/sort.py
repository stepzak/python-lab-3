from typing import Callable, Any

from src.sort.base import T
from src.sort.factory import SortFactory


def sort(arr: list[T],
        key: Callable[[T], Any] | None = None,
        reverse: bool = False,
        cmp: Callable[[T, T], int] | None = None,
        *,
        algorithm: str = 'quick',
) -> list[T]:
    algo = SortFactory.create_sorter(algorithm)
    return algo.sort(arr, key, reverse, cmp)

if __name__ == '__main__':
    print(sort([1, 5, 4, 2, 1], algorithm='bubble'))
    print(sort([1, 5, 4, 2, 1]))
    print(sort([1, 5, 4, 2, 1], algorithm='counting'))