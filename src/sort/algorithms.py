import logging
from math import floor, log2
from typing import Any, Callable

from src.sort.base import SortingAlgorithm, T

logger = logging.getLogger(__name__)

class QuickSort(SortingAlgorithm):
    def _algorithm(self, arr: list, key = None, **kwargs) -> list[T]:
        return self._quick_sort(arr, key = key)
    
    def _quick_sort(self, arr: list[T], low: int = 0, high: int | None = None, key = None) -> list[T]:
        if high is None:
            high = len(arr) - 1

        if low >= high:
            return [arr[low]] if low == high else []
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            current_val = key(arr[j]) if key else arr[j]
            pivot_val = key(pivot) if key else pivot

            if current_val <= pivot_val:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1

        return (self._quick_sort(arr, low, pivot_index - 1, key) +
                [arr[pivot_index]] +
                self._quick_sort(arr, pivot_index + 1, high, key))

class BubbleSort(SortingAlgorithm):

    def _algorithm(self, arr: list[T], key: Callable[[T], Any] | None = None, **kwargs ) -> list[T]:
        while True:
            br = True
            for k in range(1, len(arr)):
                current_val = key(arr[k]) if key else arr[k]
                prev_val = key(arr[k - 1]) if key else arr[k - 1]
                if prev_val > current_val:
                    arr[k], arr[k - 1] = arr[k - 1], arr[k]
                    br = False
            if br:
                return arr

class CountingSort(SortingAlgorithm):
    __supports_comparator__ = False
    __supports_key__ = True

    def _algorithm(self, arr: list[T], key: Callable[[T], Any] | None = None, **kwargs) -> list[T]:
        mapped_arr = arr.copy()
        if key:
            mapped_arr = list(map(key, mapped_arr))
        if any((x < 0 for x in mapped_arr)):
            raise ValueError("CountingSort can only sort non-negative integers")
        max_val = max(mapped_arr)
        count_arr = [0] * (max_val +1)
        for num in mapped_arr:
            count_arr[num] += 1

        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]
        out = [0]*len(arr)

        for i in range(len(mapped_arr) - 1, -1, -1):
            search = mapped_arr[i]
            out[count_arr[search] - 1] = arr[i]
            count_arr[search] -= 1

        return out

class RadixSort(SortingAlgorithm):
    __supports_comparator__ = False
    __supports_key__ = True


    def _algorithm(self, arr: list[T], key: Callable[[T], Any] | None = None, **kwargs) -> list[T]:
        check = (x<0 for x in arr)
        if any(check):
            raise ValueError("RadixSort can only sort non-negative integers")
        base: int = kwargs.get("base", 10)
        max_value = max(arr)
        log = log2(max_value)/log2(base)
        max_len = floor(log)+1
        multiplier = 1
        for i in range(max_len):
            counting_sort = CountingSort()
            key = lambda x: (x // multiplier) % base
            arr = counting_sort.sort(arr = arr, key = key)
            multiplier *= base
        return arr
