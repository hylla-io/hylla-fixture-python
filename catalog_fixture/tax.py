import math


def round_half_up(x: float) -> int:
    return max(0, math.floor(x + 0.5))


def apply_tax(cents: int, rate_percent: int) -> int:
    """Adds tax at `rate_percent` to an amount in cents, rounding half up.

    A negative amount (a refund) becomes zero.
    """
    return round_half_up(cents * (100 + rate_percent) / 100)
