from typing import Literal, get_args

SORT_TYPES_TYPE = Literal["quick", "bubble", "radix", "heap", "bucket", "counting"]
ARR_TYPES_TYPE = Literal[
        "sorted", "nearly_sorted_1%", "nearly_sorted_5%", "nearly_sorted_10%",
        "unique_1%", "unique_5%", "unique_10%", "reverse_sorted",
        "random_int", "random_int_distinct", "random_float", "random_float_normalized",
        "all"
    ]
ARR_TYPES = get_args(ARR_TYPES_TYPE)[:-1]
ARR_TYPES_INT = ARR_TYPES[:-3]