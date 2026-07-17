"""
ex03 — Position sizing (functions, edge cases, exceptions)

Real code is mostly edge cases. This exercise makes you handle them
deliberately instead of hoping. It's also a function your trading agent
genuinely needs.

Rule you're implementing (a classic risk rule):
  Risk at most `risk_pct` of the account on any one trade, where "risk"
  is the distance between entry price and stop-loss price.

Run:  python3 ex03_position_sizing.py
"""

import math
#imports the math library for rounding to min/max etc.


#function to determine shares to buy based on account value and risk levels
def shares_to_buy( account_value, risk_pct, entry_price, stop_price):
    """How many WHOLE shares can I buy risking at most risk_pct of account?

    Logic:
      dollars_at_risk   = account_value * (risk_pct / 100)
      risk_per_share    = entry_price - stop_price
      shares            = floor(dollars_at_risk / risk_per_share)

    But also, a real function validates its inputs. Raise ValueError with a
    HUMAN-READABLE message (any wording) when:
      - account_value <= 0
      - risk_pct <= 0 or risk_pct > 100
      - entry_price <= 0
      - stop_price >= entry_price   (stop above entry = not a long trade)

    And one cap: never return more shares than the account can afford
    outright (floor(account_value / entry_price)).

    Example: account 1000, risk 2% (=$20), entry 50, stop 48 (risk $2/share)
             -> 10 shares. But with entry 5, stop 4.50 (risk $0.50/share),
             $20/0.50 = 40 shares = $200 -> affordable, fine. If the account
             only allowed fewer via floor(account_value / entry_price), that
             cap wins instead.
    """
    #dollars_at_risk = account_value * (risk_pct / 100)
    #risk_per_share = entry_price - stop_price
    #shares = math.floor(dollars_at_risk / risk_per_share)

    #boolean logic for value errors
    if account_value <= 0:
        raise ValueError(f"account_value must be > 0, got {account_value}")
    if risk_pct <= 0 or risk_pct > 100:
        raise ValueError(f"risk_pct must be between 0-100, got {risk_pct}")
    if entry_price <= 0:
        raise ValueError(f"entry price must be > 0, got {entry_price}")
    if stop_price >= entry_price:
        raise ValueError(f"stop_price must be less than entry_price, got {stop_price}")

    #calcs for variables in use
    dollars_at_risk = account_value * (risk_pct / 100)
    risk_per_share = entry_price - stop_price
    shares = math.floor(dollars_at_risk / risk_per_share)

    #calculates if a stock purchase is affordable, then returns the min number of shares that qualify
    affordable = math.floor(account_value / entry_price)
    return min(shares, affordable)

#function to determine if quantity of shares to buy is safe relative to account holdings
def safe_shares_to_buy(account_value, risk_pct, entry_price, stop_price):
    """Wrapper that never raises: returns (shares, None) on success or
    (0, error_message_string) if shares_to_buy raised ValueError.

    This is the "boundary" pattern: validation lives in the core function,
    and ONE place decides how to present failures. try/except goes here —
    and only here, and it catches ONLY ValueError. A bare `except:` would
    hide real bugs (like a typo'd variable name) — that's why the last
    test checks that TypeErrors still escape.
    """
    # try/catch for ValueError...returns result+None if no error, catches the error if present
    try:
        result = shares_to_buy(account_value, risk_pct, entry_price, stop_price)
        return (result, None)

    except ValueError as e:
        return (0, str(e))


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
            print(f"  FAIL  {name}  (expected ValueError, nothing raised)")
        except ValueError:
            checks.append(True)
            print(f"  PASS  {name}")
        except Exception as e:
            checks.append(False)
            print(f"  FAIL  {name}  (expected ValueError, got {type(e).__name__})")

    print("shares_to_buy — happy path:")
    check("textbook case", shares_to_buy(1000, 2, 50, 48), 10)
    check("floors fractional shares", shares_to_buy(1000, 2, 50, 47), 6)   # 20/3 = 6.67 -> 6
    check("affordability headroom", shares_to_buy(400, 2, 5, 4.50), 16)    # risk allows 16; afford cap (80) not hit
    check("cap kicks in", shares_to_buy(100, 50, 5, 4.50), 20)             # risk allows 100; afford floor(100/5)=20

    print("shares_to_buy — bad inputs raise ValueError:")
    check_raises("zero account", lambda: shares_to_buy(0, 2, 50, 48))
    check_raises("negative risk", lambda: shares_to_buy(1000, -1, 50, 48))
    check_raises("risk > 100", lambda: shares_to_buy(1000, 150, 50, 48))
    check_raises("stop above entry", lambda: shares_to_buy(1000, 2, 50, 51))
    check_raises("stop equals entry", lambda: shares_to_buy(1000, 2, 50, 50))

    print("safe_shares_to_buy:")
    check("passes through success", safe_shares_to_buy(1000, 2, 50, 48), (10, None))
    got = safe_shares_to_buy(0, 2, 50, 48)
    ok = got[0] == 0 and isinstance(got[1], str) and len(got[1]) > 0
    checks.append(ok)
    print(f"  {'PASS' if ok else 'FAIL'}  returns (0, message) on bad input" + ("" if ok else f"  (got {got!r})"))
    try:
        safe_shares_to_buy(1000, 2, "fifty", 48)  # TypeError, NOT ValueError
        checks.append(False)
        print("  FAIL  must not swallow TypeError (bare except?)")
    except TypeError:
        checks.append(True)
        print("  PASS  does not swallow unrelated errors")

    print()
    if all(checks):
        print("ALL TESTS PASSED ✅  — commit it.")
    else:
        print(f"{checks.count(False)} failing. Read the FAIL lines and go again.")


if __name__ == "__main__":
    _tests()
