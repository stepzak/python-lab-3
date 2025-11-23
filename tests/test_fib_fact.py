import pytest

from src.fib_fact import factorial, fibonacci
from math import factorial as math_fact

class TestFactorial:
    cases = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    ]

    @pytest.mark.parametrize("n", cases)
    def test_fact_recursive(self, n: int) -> None:
        res = factorial.factorial_recursive(n)
        assert res == math_fact(n)

    @pytest.mark.parametrize("n", cases)
    def test_fact_iterative(self, n: int) -> None:
        res = factorial.factorial_iterative(n)
        assert res == math_fact(n)

    @pytest.mark.slow
    def test_factorial_large_number(self):

        assert factorial.factorial_iterative(10) == math_fact(10)
        assert factorial.factorial_recursive(10) == math_fact(10)


class TestFibonacci:
    fibonacci_test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (15, 610),
        (20, 6765),
    ]

    @pytest.mark.parametrize("n,expected", fibonacci_test_cases)
    def test_fibo_iterative_basic(self, n, expected):
        assert fibonacci.fibo_iterative(n) == expected

    @pytest.mark.parametrize("n,expected", fibonacci_test_cases)
    def test_fibo_recursive_basic(self, n, expected):
        assert fibonacci.fibo_recursive(n) == expected

    @pytest.mark.slow
    def test_fibonacci_large_numbers(self):
        assert fibonacci.fibo_iterative(30) == 832040
        assert fibonacci.fibo_iterative(30) == 832040