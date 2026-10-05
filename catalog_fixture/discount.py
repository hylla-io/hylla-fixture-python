from .tax import round_half_up


def apply_discount(cents: int, percent: int) -> int:
    """Takes `percent` off an amount in cents, rounding the discount half up."""
    return cents - round_half_up(cents * percent / 100)
