"""
ex02 — Positions & P&L (lists, dicts, loops, accumulation)

Given a list of parsed trades (the dicts from ex01), compute what you own
and how you've done. This is the pattern behind half of all real code:
loop over records, accumulate into a dict.

Run:  python3 ex02_positions.py
"""

TRADES = [
    {"date": "2026-06-22", "side": "BUY",  "qty": 3, "symbol": "NVDA", "price": 120.00},
    {"date": "2026-06-23", "side": "BUY",  "qty": 2, "symbol": "AAPL", "price": 210.00},
    {"date": "2026-06-24", "side": "BUY",  "qty": 2, "symbol": "NVDA", "price": 118.00},
    {"date": "2026-06-25", "side": "SELL", "qty": 4, "symbol": "NVDA", "price": 125.00},
    {"date": "2026-06-26", "side": "BUY",  "qty": 1, "symbol": "SOFI", "price": 9.50},
    {"date": "2026-06-29", "side": "SELL", "qty": 2, "symbol": "AAPL", "price": 205.00},
]


def current_positions(trades):
    """Return {symbol: net_shares} for symbols with a non-zero net position.
=
    BUY adds shares, SELL subtracts. Symbols that net to exactly 0 are
    EXCLUDED from the result.

    For TRADES above: NVDA nets to 1 (3+2-4), AAPL nets to 0 (drop it),
    SOFI nets to 1  →  {"NVDA": 1, "SOFI": 1}
    """
    # YOU: implement this

    net_shares = {}
    for t in trades:
        symbol = t["symbol"]
        if t ["side"] == "BUY":
            net_shares[symbol] = net_shares.get(symbol, 0) + t["qty"]
        elif t ["side"] == "SELL":
            net_shares[symbol] = net_shares.get(symbol, 0) - t["qty"]


    kept = {}
    for symbol, qty in net_shares.items():
        if qty != 0:
            kept[symbol] = qty
    return kept

    return net_shares

def cash_flow(trades):
    """Return net cash flow, rounded to 2 dp. BUYs cost money (negative),
    SELLs bring money in (positive).

    For TRADES above:
      -360.00 (buy NVDA) -420.00 (buy AAPL) -236.00 (buy NVDA)
      +500.00 (sell NVDA) -9.50 (buy SOFI) +410.00 (sell AAPL) = -115.50
    """
    # YOU: implement this
    raise NotImplementedError


def biggest_trade(trades):
    """Return the SYMBOL of the trade with the largest dollar value
    (qty * price). Ties: first one wins.
    """
    # YOU: implement this
    raise NotImplementedError


def trades_by_symbol(trades):
    """Group trades into {symbol: [trade, trade, ...]} preserving order.

    This exact pattern (group records by key) will show up in every
    codebase you ever touch. Hint: dict + append, or look up dict.setdefault.
    """
    # YOU: implement this
    raise NotImplementedError


# ---------------------------------------------------------------- tests --
def _tests():
    checks = []

    def check(name, got, want):
        ok = got == want
        checks.append(ok)
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + ("" if ok else f"  (got {got!r}, want {want!r})"))

    print("current_positions:")
    check("nets and drops zeros", current_positions(TRADES), {"NVDA": 1, "SOFI": 1})
    check("empty in, empty out", current_positions([]), {})

    print("cash_flow:")
    check("net flow", cash_flow(TRADES), -115.50)
    check("empty is 0", cash_flow([]), 0)

    print("biggest_trade:")
    check("finds NVDA sell (500.00)", biggest_trade(TRADES), "NVDA")

    print("trades_by_symbol:")
    grouped = trades_by_symbol(TRADES)
    check("three symbols", sorted(grouped), ["AAPL", "NVDA", "SOFI"])
    check("NVDA has 3 trades", len(grouped.get("NVDA", [])), 3)
    check("order preserved", grouped.get("NVDA", [{}])[0].get("date"), "2026-06-22")

    print()
    if all(checks):
        print("ALL TESTS PASSED ✅  — commit it.")
    else:
        print(f"{checks.count(False)} failing. Read the FAIL lines and go again.")


if __name__ == "__main__":
    _tests()
