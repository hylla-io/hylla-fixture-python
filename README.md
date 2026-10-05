# hylla-fixture-python

A tiny catalog used as a Hylla ingest fixture. Every file is small and its contents are known
exactly.

## Money

`format_money` prints cents as dollars. It lives in
[catalog_fixture/money.py](catalog_fixture/money.py).

## Tax

`apply_tax` in [catalog_fixture/tax.py](catalog_fixture/tax.py) adds tax and rounds with
`round_half_up`, which lives beside it. Refunds clamp to zero: `apply_tax(-1000, 10)` is `0`.

## Totals

`Catalog.total` takes a bulk discount with `apply_discount` at three or more items, then taxes.
`render_report` prints a report; rounding is described under [Tax](#tax).
