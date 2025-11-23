import random
import src.constants as cst

def rand_int_array(n: int, low: int, high: int, *, distinct: bool = False, seed = None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    if distinct:
        available_numbers = high - low + 1
        if available_numbers < n:
            raise ValueError(
                f"Cannot generate {n} distinct numbers from range size {available_numbers}"
            )
        result = random.sample(range(low, high + 1), n)
    else:
        result = [random.randint(low, high) for _ in range(n)]

    return result

def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    result = [a for a in range(n)]

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        result[i], result[j] = result[j], result[i]

    return result

def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    result = random.sample(range(n), k_unique)
    return result

def reserve_sorted(n: int) -> list[int]:
    result = [a for a in range(n)]
    return result[::-1]

def rand_float_array(n: int, low=0.0, high=1.0, *, seed=None) -> list[float]:
    if seed is not None:
        random.seed(seed)

    result = [random.uniform(low, high) for _ in range(n)]
    return result

class ArrayGenerator:

    @staticmethod
    def array_gen(size: int = 1000) -> dict[cst.ARR_TYPES_TYPE, list]:
        results = {
            'sorted': list(range(size)),
            'nearly_sorted_1%': nearly_sorted(size, max(1, size // 100), seed=42),
            'nearly_sorted_5%': nearly_sorted(size, max(1, size // 20), seed=42),
            'nearly_sorted_10%': nearly_sorted(size, max(1, size // 10), seed=42),
            'unique_1%': many_duplicates(size, max(1, size // 100), seed=42),
            'unique_5%': many_duplicates(size, max(1, size // 20), seed=42),
            'unique_10%': many_duplicates(size, max(1, size // 10), seed=42),
            'reverse_sorted': reserve_sorted(size),
            'random_int': rand_int_array(size, 0, size, seed=42),
            'random_int_distinct': rand_int_array(size, 0, size + 1, distinct=True, seed=42),
            'random_float': rand_float_array(size, 0, size, seed=42),
            'random_float_normalized': rand_float_array(size, 0.0, 1.0, seed=42),
        }

        return results

