from abc import ABC, abstractmethod


class Priced(ABC):
    """Anything with a price in whole cents."""

    @abstractmethod
    def price_cents(self) -> int: ...


class Book(Priced):
    def __init__(self, title: str, unit_cents: int, quantity: int) -> None:
        self.title = title
        self.unit_cents = unit_cents
        self.quantity = quantity

    def price_cents(self) -> int:
        return self.unit_cents * self.quantity
