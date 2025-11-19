from src.sort.algorithms import QuickSort, BubbleSort, CountingSort
from src.sort.base import SortingAlgorithm


class SortFactory:
    _algorithms = {
        'quick': QuickSort,
        'bubble': BubbleSort,
        "counting": CountingSort
    }

    @classmethod
    def create_sorter(cls, algorithm: str) -> SortingAlgorithm:
        if algorithm not in cls._algorithms:
            raise ValueError(f"Unknown algorithm: {algorithm}. Available: {list(cls._algorithms.keys())}")
        return cls._algorithms[algorithm]()

    @classmethod
    def register_algorithm(cls, name: str, algorithm_class):
        cls._algorithms[name] = algorithm_class