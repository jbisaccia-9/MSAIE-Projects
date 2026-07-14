#dict highlighting various hypothetical trades from moneybot agent trading bot
TRADES = [
    {"date": "2026-06-22", "side": "BUY",  "qty": 3, "symbol": "NVDA", "price": 120.00},
    {"date": "2026-06-23", "side": "BUY",  "qty": 2, "symbol": "AAPL", "price": 210.00},
    {"date": "2026-06-24", "side": "BUY",  "qty": 2, "symbol": "NVDA", "price": 118.00},
    {"date": "2026-06-25", "side": "SELL", "qty": 4, "symbol": "NVDA", "price": 125.00},
    {"date": "2026-06-26", "side": "BUY",  "qty": 1, "symbol": "SOFI", "price": 9.50},
    {"date": "2026-06-29", "side": "SELL", "qty": 2, "symbol": "AAPL", "price": 205.00},
]

#determines the total net shares of a stock post trade
def current_positions(trades):
    """Return {symbol: net_shares} for symbols with a non-zero net position.

    BUY adds shares, SELL subtracts. Symbols that net to exactly 0 are
    EXCLUDED from the result.

    For TRADES above: NVDA nets to 1 (3+2-4), AAPL nets to 0 (drop it),
    SOFI nets to 1  →  {"NVDA": 1, "SOFI": 1}
    """
    net_shares = {}
    for t in trades:
        symbol = t["symbol"]
        if t ["side"] == "BUY":
            net_shares[symbol] = net_shares.get(symbol, 0) + t["qty"]
        elif t ["side"] == "SELL":
            net_shares[symbol] = net_shares.get(symbol, 0) - t["qty"]

#returns the qty of a stock as long as it is not zero
    kept = {}
    for symbol, qty in net_shares.items():
        if qty != 0:
            kept[symbol] = qty
    return kept

#determines the total value of a stock holding post trade, rounded 2 decimal places
def cash_flow(trades):
    """Return net cash flow, rounded to 2 dp. BUYs cost money (negative),
    SELLs bring money in (positive).

    For TRADES above:
      -360.00 (buy NVDA) -420.00 (buy AAPL) -236.00 (buy NVDA)
      +500.00 (sell NVDA) -9.50 (buy SOFI) +410.00 (sell AAPL) = -115.50
    """
    total = 0  # single-number accumulator — replaces the dict reference
    for t in trades:  # the loop
        if t["side"] == "BUY":
            total = total - (t["qty"] * t["price"])
        elif t["side"] == "SELL":
            total = total + (t["qty"] * t["price"])
    return round(total, 2)  # rounds the FINAL total, once, after the loop

#iterates through the trades list to determine the largest trade
def biggest_trade(trades):
    """Return the SYMBOL of the trade with the largest dollar value
    (qty * price). Ties: first one wins.
    """
    #returns symbol of largest trade: max measures each trade via the lambda
    #(qty * price), returns the winning trade DICT, then ["symbol"] plucks the answer
    return max(trades, key=lambda h: h["qty"] * h["price"])["symbol"]


def trades_by_symbol(trades):
    """Group trades into {symbol: [trade, trade, ...]} preserving order.

    This exact pattern (group records by key) will show up in every
    codebase you ever touch.
    """
    #iterates through trades and groups each trade under its symbol
    symbols = {}
    for s in trades:
        if s["side"] == "BUY":
            symbols[s["symbol"]] = symbols.get(s["symbol"], []) + [s]
        elif s["side"] == "SELL":
            symbols[s["symbol"]] = symbols.get(s["symbol"], []) + [s]

#returns the symbol of the symbol by trades
    return symbols


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
