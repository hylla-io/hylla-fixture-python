import math


def round_half_up(x: float) -> int:
    return max(0, math.floor(x + 0.5))


def format_money(cents: int) -> str:
    sign = "-" if cents < 0 else ""
    whole, frac = divmod(abs(cents), 100)
    return f"{sign}${whole}.{frac:02d}"
