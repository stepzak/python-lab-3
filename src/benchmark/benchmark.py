import timeit
from typing import Callable
from src.sort.sort import sort
from src.benchmark.test_generator import ArrayGenerator
from tabulate import tabulate
import src.constants as cst

def timeit_once(func: Callable, *args, **kwargs) -> float:
    start = timeit.default_timer()
    func(*args, **kwargs)
    end = timeit.default_timer()
    return end - start


def benchmark_sorts(arrays: dict[cst.SORT_TYPES_TYPE, list[cst.ARR_TYPES_TYPE]] | None = None, iters: int = 1) -> dict[str, dict[str, float | str]]:
    if not arrays:
        arrays: dict[cst.SORT_TYPES_TYPE, list[cst.ARR_TYPES_TYPE]] = {
            "quick": ["all"],
            "bubble": ["all"],
            "radix": cst.ARR_TYPES_INT,
            "heap": ["all"],
            "bucket": ["random_float_normalized"],
            "counting": cst.ARR_TYPES_INT
        }
    results = {algo_name: {} for algo_name in arrays.keys()}

    gen_arrays = ArrayGenerator.array_gen()
    for k, v in arrays.items():
        if "all" in v:
            v = cst.ARR_TYPES
        for arr_type in v:
            arr = gen_arrays[arr_type].copy()
            results[k][arr_type] = 0.0
            for it in range(iters):
                res = timeit_once(sort, arr = arr, algorithm = k)
                results[k][arr_type]+=res
            results[k][arr_type] = results[k][arr_type] / iters

    return results

def create_table(data: dict[str, dict[str, float]], tablefmt: str = "github"):
    headers = ("Algorithm",) + cst.ARR_TYPES
    rows = []
    for k, v in data.items():
        row = [k] + len(cst.ARR_TYPES) * [float('nan')]
        for t in v:
            ind = cst.ARR_TYPES.index(t)+1
            row[ind] = v[t]
        rows.append(row)

    return tabulate(rows, headers, tablefmt=tablefmt)


if __name__ == "__main__":

    res_b = benchmark_sorts(iters = 5)
    print(create_table(res_b))