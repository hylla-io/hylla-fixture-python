from .discount import apply_discount
from .pricing import Priced
from .tax import apply_tax


class Catalog:
    def __init__(self) -> None:
        self.items: list[Priced] = []

    def add(self, item: Priced) -> None:
        self.items.append(item)

    def count(self) -> int:
        return len(self.items)

    def subtotal(self) -> int:
        return sum(item.price_cents() for item in self.items)

    def total(self, rate_percent: int) -> int:
        bulk = 10 if self.count() >= 3 else 0
        return apply_tax(apply_discount(self.subtotal(), bulk), rate_percent)
