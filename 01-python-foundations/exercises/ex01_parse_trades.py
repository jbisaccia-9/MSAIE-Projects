"""
ex01 — Parse trade-log lines (strings, splitting, f-strings)

Your trading agent writes log lines like:
    "2026-06-24 BUY 3 NVDA @ 121.79"
    "2026-06-25 SELL 2 AAPL @ 214.30"

You'll write three small functions that pick these apart and rebuild them.
No imports needed. Hands only.

Run:  python3 ex01_parse_trades.py
"""


def parse_trade(line):
    """Parse one log line into a dict.

    Input:  "2026-06-24 BUY 3 NVDA @ 121.79"
    Output: {"date": "2026-06-24", "side": "BUY", "qty": 3,
             "symbol": "NVDA", "price": 121.79}

    Notes: qty must be an int, price must be a float.
    Extra whitespace around the line should not break you (see tests).
    """
    # YOU: implement this
    raise NotImplementedError


def trade_value(trade):
    """Return the dollar value of a parsed trade (qty * price),
    rounded to 2 decimal places.

    Input:  {"date": ..., "side": ..., "qty": 3, "symbol": ..., "price": 121.79}
    Output: 365.37
    """
    # YOU: implement this
    raise NotImplementedError


def format_trade(trade):
    """The reverse of parse_trade: turn the dict back into a log line.

    Input:  {"date": "2026-06-24", "side": "BUY", "qty": 3,
             "symbol": "NVDA", "price": 121.79}
    Output: "2026-06-24 BUY 3 NVDA @ 121.79"

    Price always shows exactly 2 decimal places ("121.79", "5.50", "100.00").
    Hint: f-string format specs. Look up what {x:.2f} does.
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

    print("parse_trade:")
    t = parse_trade("2026-06-24 BUY 3 NVDA @ 121.79")
    check("basic parse", t, {"date": "2026-06-24", "side": "BUY", "qty": 3, "symbol": "NVDA", "price": 121.79})
    check("qty is int", type(t["qty"]), int)
    check("price is float", type(t["price"]), float)
    check("handles whitespace", parse_trade("  2026-06-25 SELL 2 AAPL @ 214.30\n"),
          {"date": "2026-06-25", "side": "SELL", "qty": 2, "symbol": "AAPL", "price": 214.30})

    print("trade_value:")
    check("3 @ 121.79", trade_value({"qty": 3, "price": 121.79}), 365.37)
    check("rounds to cents", trade_value({"qty": 3, "price": 33.333}), 100.0)

    print("format_trade:")
    check("round trip", format_trade({"date": "2026-06-24", "side": "BUY", "qty": 3, "symbol": "NVDA", "price": 121.79}),
          "2026-06-24 BUY 3 NVDA @ 121.79")
    check("pads price to 2dp", format_trade({"date": "2026-07-01", "side": "SELL", "qty": 10, "symbol": "F", "price": 5.5}),
          "2026-07-01 SELL 10 F @ 5.50")

    print()
    if all(checks):
        print("ALL TESTS PASSED ✅  — commit it:  git add -p && git commit")
    else:
        print(f"{checks.count(False)} failing. Read the FAIL lines and go again.")


if __name__ == "__main__":
    _tests()
