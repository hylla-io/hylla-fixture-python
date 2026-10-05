from .pricing import Priced


def legacy_total(items: list[Priced]) -> int:
    """The pre-catalog total: sums prices with no tax. Kept for old callers."""
    total = 0
    for item in items:
        total += item.price_cents()
    return total
