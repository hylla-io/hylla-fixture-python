from . import odd


def is_even(n: int) -> bool:
    return True if n == 0 else odd.is_odd(n - 1)
