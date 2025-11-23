import pytest
from src.sort.sort import sort
from src.constants import ARR_TYPES, ARR_TYPES_INT
from src.benchmark.test_generator import ArrayGenerator
from src.sort.factory import SortFactory

@pytest.fixture(scope = "session")
def array_generator():
    return ArrayGenerator.array_gen(size = 100)


@pytest.mark.parametrize(
    "algo,arr_types",
    [
        ("quick", ARR_TYPES),
        ("bubble", ARR_TYPES),
        ("counting", ARR_TYPES_INT),
        ("radix", ARR_TYPES_INT),
        ("bucket", [ARR_TYPES[-1]]),
        ("heap", ARR_TYPES)
    ]
)
def test_all(array_generator, algo, arr_types):
    for arr_type in arr_types:
        arr = array_generator[arr_type]
        assert sort(arr, algorithm=algo) == sorted(arr)
        assert sort(arr, algorithm=algo, reverse=True) == sorted(arr, reverse=True)
        if SortFactory.create_sorter(algo).__supports_key__:
            if algo != "counting":
                assert sort(arr, algorithm=algo, key = lambda x: -x) == sorted(arr,key=lambda x: -x)
    if algo == "counting":
        attr_arr = [{"a": 1}, {"a": 3}, {"a": 2}, {"a": 0}]
        assert sort(attr_arr, algorithm=algo, key = lambda x: x["a"]) == sorted(attr_arr, key=lambda x: x["a"])