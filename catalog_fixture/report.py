from .catalog import Catalog
from .even import is_even
from .money import format_cents


def render_report(catalog: Catalog, rate_percent: int) -> str:
    parity = "even" if is_even(catalog.count()) else "odd"
    return "\n".join(
        [
            f"items: {catalog.count()} ({parity})",
            f"subtotal: {format_cents(catalog.subtotal())}",
            f"total: {format_cents(catalog.total(rate_percent))}",
        ]
    )
