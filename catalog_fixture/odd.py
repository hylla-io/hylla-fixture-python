from . import even


def is_odd(n: int) -> bool:
    return False if n == 0 else even.is_even(n - 1)
