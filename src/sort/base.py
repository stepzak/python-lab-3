from abc import ABC, abstractmethod
from functools import cmp_to_key
from typing import TypeVar, Callable, Any

T = TypeVar("T")

class SortingAlgorithm(ABC):
    def sort(self, arr: list[T],
             key: Callable[[T], Any] | None = None,
             reverse: bool = False,
             cmp: Callable[[T, T], int] | None = None) -> list[T]:
        arr_copy = arr.copy()
        unified_key = self._resolve_cmp(key, cmp)
        res = self._algorithm(arr_copy, unified_key)
        return res if not reverse else res[::-1]

    @abstractmethod
    def _algorithm(self, arr: list[T], key: Callable[[T], Any] | None = None,) -> list[T]:
        pass

    @staticmethod
    def _resolve_cmp(
                     key: Callable[[T], Any] | None = None,
                     cmp: Callable[[T, T], int] | None = None) -> Callable[[T], Any]:

        if key and cmp:
            def combined_cmp(a, b):
                a_key = key(a)
                b_key = key(b)
                return cmp(a_key, b_key)

            return cmp_to_key(combined_cmp)

        elif cmp:
            return cmp_to_key(cmp)

        elif key:
            return key
        else:
            return lambda a: a

