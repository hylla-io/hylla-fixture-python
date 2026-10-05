from .catalog import Catalog
from .even import is_even
from .money import format_money


def render_report(catalog: Catalog, rate_percent: int) -> str:
    parity = "even" if is_even(catalog.count()) else "odd"
    return "\n".join(
        [
            f"items: {catalog.count()} ({parity})",
            f"subtotal: {format_money(catalog.subtotal())}",
            f"total: {format_money(catalog.total(rate_percent))}",
        ]
    )
