import math


def round_half_up(x: float) -> int:
    return math.floor(x + 0.5)


def format_cents(cents: int) -> str:
    sign = "-" if cents < 0 else ""
    whole, frac = divmod(abs(cents), 100)
    return f"{sign}${whole}.{frac:02d}"
