from typing import Any
import json
from src.sort.sort import sort
from dataclasses import dataclass
from src.benchmark.benchmark import benchmark_sorts, create_table
from src.stack.factory import StackFactory
from src.stack.abc import Stack
from src.fib_fact.fibonacci import fibo_iterative, fibo_recursive
from src.fib_fact.factorial import factorial_iterative, factorial_recursive

@dataclass
class Output:
    result: Any = ""
    meta: dict[str, Any] | None = None


def sort_command(*args) -> Output:

    arr_begin: str = args[0]
    if arr_begin[0] != "[":
        return Output("No array found in arguments")
    if arr_begin[-1] != "]":
        for arg in args[1:]:
            arr_begin += arg
            if arg[-1] == "]":
                break
        else:
            return Output("Invalid array")

    arr = json.loads(arr_begin)
    reverse = False
    if args[-1].lower() in ("true", "t", "yes", "y", "1"):
        reverse = True
    ret = sort(arr, reverse = reverse, algorithm = args[-2])
    return Output(ret)


def benchmark_command(*args) -> Output:
    n = int(args[0])
    result = benchmark_sorts(iters = n)
    table = create_table(result)
    return Output(table)

def stack_command(*args) -> Output:
    name = args[0]
    action = args[1]
    if action == "create":
        impl = args[2]
        stack = StackFactory.create(impl)
        meta = {"variable": name, "mode": "create"}
        return Output(stack, meta)

    action_to_arg_index = {
        "push": 2
    }
    if not callable(getattr(Stack, action, None)):
        return Output("Invalid action")
    meta = {"variable": name, "attr": action}
    arg_index = action_to_arg_index.get(action, None)
    if arg_index:
        meta["args"] = (float(x) for x in args[arg_index:])
    return Output("", meta)

def fibonacci_command(*args) -> Output:
    val = int(args[0])
    mode = args[1]
    if mode == "iterative":
        return Output(fibo_iterative(val))
    elif mode == "recursive":
        return Output(fibo_recursive(val))
    else:
        return Output("Invalid mode")

def factorial_command(*args) -> Output:
    val = int(args[0])
    mode = args[1]
    if mode == "iterative":
        return Output(factorial_iterative(val))
    elif mode == "recursive":
        return Output(factorial_recursive(val))
    else:
        return Output("Invalid mode")



