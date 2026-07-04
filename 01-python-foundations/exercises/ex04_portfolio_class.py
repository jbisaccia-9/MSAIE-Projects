"""
ex04 — A Portfolio class (classes, state, methods)

So far your functions passed data around. A class BUNDLES data with the
functions that operate on it. `self` is just "the particular portfolio
this method was called on."

You're building the object your refactored trading agent will eventually
use for real (module 04).

Run:  python3 ex04_portfolio_class.py
"""


class Portfolio:
    """Tracks cash and share positions with average cost basis.

    Behavior spec:

    p = Portfolio(cash=1000)
    p.cash                    -> 1000.0
    p.buy("NVDA", qty=2, price=100)   # cash -= 200; now holds 2 NVDA @ avg 100
    p.buy("NVDA", qty=2, price=110)   # cash -= 220; 4 NVDA @ avg 105
    p.qty("NVDA")             -> 4
    p.avg_cost("NVDA")        -> 105.0
    p.sell("NVDA", qty=3, price=120)  # cash += 360; 1 NVDA left, avg stays 105
    p.realized_pnl            -> 45.0   # (120 - 105) * 3
    p.qty("AAPL")             -> 0      # unknown symbol = 0, never KeyError

    Rules:
      - buy() raises ValueError if it would take cash below 0
      - sell() raises ValueError if selling more shares than held
      - avg_cost on a symbol you don't hold raises ValueError
      - selling your whole position removes the symbol entirely
      - realized_pnl accumulates across all sells: (sell_price - avg_cost) * qty
      - round money to 2 dp where it's user-visible (cash, avg_cost, realized_pnl)

    Also implement __repr__ so debugging isn't miserable. Format:
      Portfolio(cash=580.00, positions={'NVDA': 1})
    (positions maps symbol -> qty in the repr)
    """

    def __init__(self, cash):
        # YOU: implement this  (what state do you need to track avg cost?)
        raise NotImplementedError

    def buy(self, symbol, qty, price):
        # YOU: implement this
        raise NotImplementedError

    def sell(self, symbol, qty, price):
        # YOU: implement this
        raise NotImplementedError

    def qty(self, symbol):
        # YOU: implement this
        raise NotImplementedError

    def avg_cost(self, symbol):
        # YOU: implement this
        raise NotImplementedError

    def __repr__(self):
        # YOU: implement this
        raise NotImplementedError


# ---------------------------------------------------------------- tests --
def _tests():
    checks = []

    def check(name, got, want):
        ok = got == want
        checks.append(ok)
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + ("" if ok else f"  (got {got!r}, want {want!r})"))

    def check_raises(name, fn):
        try:
            fn()
            checks.append(False)
            print(f"  FAIL  {name}  (expected ValueError)")
        except ValueError:
            checks.append(True)
            print(f"  PASS  {name}")

    print("basic lifecycle:")
    p = Portfolio(cash=1000)
    check("starting cash", p.cash, 1000.0)
    p.buy("NVDA", qty=2, price=100)
    p.buy("NVDA", qty=2, price=110)
    check("cash after two buys", p.cash, 580.0)
    check("qty", p.qty("NVDA"), 4)
    check("avg cost blends", p.avg_cost("NVDA"), 105.0)
    p.sell("NVDA", qty=3, price=120)
    check("cash after sell", p.cash, 940.0)
    check("qty after sell", p.qty("NVDA"), 1)
    check("avg cost unchanged by sell", p.avg_cost("NVDA"), 105.0)
    check("realized pnl", p.realized_pnl, 45.0)
    check("unknown symbol qty is 0", p.qty("AAPL"), 0)

    print("full exit removes symbol:")
    p.sell("NVDA", qty=1, price=100)
    check("qty 0 after exit", p.qty("NVDA"), 0)
    check("realized pnl accumulates", p.realized_pnl, 40.0)  # 45 + (100-105)*1
    check_raises("avg_cost after exit raises", lambda: p.avg_cost("NVDA"))

    print("guard rails:")
    p2 = Portfolio(cash=100)
    check_raises("cannot overspend", lambda: p2.buy("AAPL", qty=1, price=101))
    check_raises("cannot oversell", lambda: p2.sell("AAPL", qty=1, price=10))

    print("__repr__:")
    p3 = Portfolio(cash=580)
    p3.buy("NVDA", qty=1, price=100)
    check("repr format", repr(p3), "Portfolio(cash=480.00, positions={'NVDA': 1})")

    print()
    if all(checks):
        print("ALL TESTS PASSED ✅  — commit it.")
    else:
        print(f"{checks.count(False)} failing. Read the FAIL lines and go again.")


if __name__ == "__main__":
    _tests()
