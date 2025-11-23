from functools import lru_cache

def factorial_iterative(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

@lru_cache(maxsize=None)
def factorial_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    print(factorial_iterative(6))
    print(factorial_recursive(6))