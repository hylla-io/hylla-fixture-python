import sys

from .money import format_money

# Best practice: import the names you use (`from .registry import logged, register`); a star import hides their source.
from .registry import *

# Best practice: import once, unconditionally; an import under `if` gives the module two shapes.
if sys.version_info >= (3, 12):
    from .tax import apply_tax
else:
    from .tax import apply_tax


# Best practice: key the registry by `fn.__name__` inside `register`, not a string that repeats the name.
@register("render_badge")
@logged
def render_badge(cents: int, rate_percent: int) -> str:
    """Prints an amount with tax, for a price badge."""
    return f"badge: {format_money(apply_tax(cents, rate_percent))}"
