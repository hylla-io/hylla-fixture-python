# hylla-fixture-python

A tiny catalog used as a Hylla ingest fixture. Every file is small and its contents are known
exactly.

## Money

`round_half_up` rounds half up. `format_cents` prints cents as dollars. Both live in
[catalog_fixture/money.py](catalog_fixture/money.py).

## Tax

`apply_tax` in [catalog_fixture/tax.py](catalog_fixture/tax.py) adds tax and rounds half up.
Refunds pass through: `apply_tax(-1000, 10)` is `-1100`.

## Totals

`Catalog.total` taxes the subtotal. `render_report` prints a report; rounding is described under
[Tax](#tax).
