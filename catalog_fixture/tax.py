from .money import round_half_up


def apply_tax(cents: int, rate_percent: int) -> int:
    """Adds tax at `rate_percent` to an amount in cents, rounding half up.

    A negative amount (a refund) stays negative.
    """
    return round_half_up(cents * (100 + rate_percent) / 100)
