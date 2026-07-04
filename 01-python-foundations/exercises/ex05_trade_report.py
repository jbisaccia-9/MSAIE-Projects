"""
ex05 — Trade report (csv, json, datetime, pathlib — real files in, real files out)

The capstone of the week: read `sample_trades.csv`, compute a summary, write
`report.json`. Every data/AI pipeline you'll ever build is this shape:
load -> transform -> serialize.

Allowed imports: csv, json, datetime, pathlib. Read their docs — that's the
actual exercise. (Also, in a REPL, try round(2.675, 2) and enjoy the surprise.
Look up "banker's rounding" — it explains itself.)

Run:  python3 ex05_trade_report.py
"""

import csv
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
CSV_PATH = HERE / "sample_trades.csv"
REPORT_PATH = HERE / "report.json"


def load_trades(path):
    """Read the CSV at `path` into a list of dicts with REAL types:

    [{"date": date(2026, 5, 4), "side": "BUY", "qty": 5,
      "symbol": "NVDA", "price": 112.50}, ...]

    - date must be a datetime.date (hint: date.fromisoformat)
    - qty int, price float
    - Use csv.DictReader; don't split strings by hand — you did that in ex01,
      now use the stdlib like a professional.
    """
    # YOU: implement this
    raise NotImplementedError


def total_volume(trades):
    """Total dollar volume across all trades (qty * price), rounded to 2 dp."""
    # YOU: implement this
    raise NotImplementedError


def summary_by_symbol(trades):
    """Return {symbol: {"trades": n, "bought": total_buy_qty,
                        "sold": total_sell_qty, "net_qty": bought - sold}}
    """
    # YOU: implement this
    raise NotImplementedError


def trades_in_month(trades, year, month):
    """How many trades happened in the given year+month?
    Use the date objects — no string slicing. (t["date"].year, .month)
    """
    # YOU: implement this
    raise NotImplementedError


def write_report(trades, out_path, as_of):
    """Write a JSON report to out_path and ALSO return the dict you wrote.

    Shape:
      {
        "as_of": "2026-07-03",          # as_of is a date; serialize as ISO string
        "total_volume": 5248.42,
        "symbols": { ... summary_by_symbol output ... }
      }

    Gotcha you're meant to hit: json.dump refuses datetime.date objects.
    You decide how to handle it cleanly.
    Use indent=2 so the file is human-readable.
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

    print("load_trades:")
    trades = load_trades(CSV_PATH)
    check("14 rows", len(trades), 14)
    check("first row parsed", trades[0],
          {"date": date(2026, 5, 4), "side": "BUY", "qty": 5, "symbol": "NVDA", "price": 112.50})
    check("date is a real date object", isinstance(trades[0]["date"], date), True)

    print("total_volume:")
    check("sums to 5248.42", total_volume(trades), 5248.42)

    print("summary_by_symbol:")
    s = summary_by_symbol(trades)
    check("5 symbols", len(s), 5)
    check("NVDA summary", s.get("NVDA"), {"trades": 6, "bought": 10, "sold": 10, "net_qty": 0})
    check("GOOG net long", s.get("GOOG"), {"trades": 1, "bought": 1, "sold": 0, "net_qty": 1})

    print("trades_in_month:")
    check("June 2026 has 7", trades_in_month(trades, 2026, 6), 7)
    check("May 2026 has 7", trades_in_month(trades, 2026, 5), 7)
    check("July 2026 has 0", trades_in_month(trades, 2026, 7), 0)

    print("write_report:")
    returned = write_report(trades, REPORT_PATH, as_of=date(2026, 7, 3))
    on_disk = json.loads(REPORT_PATH.read_text())
    check("returned == written", returned, on_disk)
    check("as_of serialized", on_disk.get("as_of"), "2026-07-03")
    check("volume in report", on_disk.get("total_volume"), 5248.42)
    check("symbols present", sorted(on_disk.get("symbols", {})), ["AAPL", "AMD", "GOOG", "NVDA", "SOFI"])

    print()
    if all(checks):
        print("ALL TESTS PASSED ✅  — that's the whole foundation week. Commit, push, log it.")
    else:
        print(f"{checks.count(False)} failing. Read the FAIL lines and go again.")


if __name__ == "__main__":
    _tests()
