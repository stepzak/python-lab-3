import logging
from abc import ABC, abstractmethod
from functools import cmp_to_key
from typing import TypeVar, Callable, Any

T = TypeVar("T")

logger = logging.getLogger(__name__)

class SortingAlgorithm(ABC):

    __supports_key__ = True
    __supports_comparator__ = True

    def sort(self, arr: list[T],
             key: Callable[[T], Any] | None = None,
             reverse: bool = False,
             cmp: Callable[[T, T], int] | None = None,
             **kwargs) -> list[T]:
        arr_copy = arr.copy()
        if not self.__supports_key__:
            logger.warning(f"{self.__class__.__name__} does not support key")
        unified_key = key
        if self.__supports_comparator__:
            unified_key = self._resolve_cmp(key, cmp)
        res = self._algorithm(arr_copy, unified_key, **kwargs)
        return res if not reverse else res[::-1]

    @abstractmethod
    def _algorithm(self, arr: list[T], key: Callable[[T], Any] | None = None, **kwargs) -> list[T]:
        pass

    @staticmethod
    def _resolve_cmp(
                     key: Callable[[T], Any] | None = None,
                     cmp: Callable[[T, T], int] | None = None) -> Callable[[T], Any] | None:

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
            return None

