"""
=========================================================
  tests/test_algorithms.py  —  Member 5 (Testing)
  Automated unit tests for all four greedy algorithms.
  Run with:  python -m pytest tests/ -v
             or simply: python tests/test_algorithms.py
=========================================================
"""

import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from algorithms.coin_change         import coin_change_greedy
from algorithms.huffman_coding      import huffman_encode
from algorithms.fractional_knapsack import fractional_knapsack, Item
from algorithms.job_scheduling      import job_scheduling, Job


# ── helpers ───────────────────────────────────────────────────────────────────────

PASS = "\033[92m  PASS\033[0m"
FAIL = "\033[91m  FAIL\033[0m"
_results: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    _results.append((label, condition))
    status = PASS if condition else FAIL
    print(f"  {status}  {label}")


# ── coin change tests ─────────────────────────────────────────────────────────────

def test_coin_change() -> None:
    print("\n  ── Coin Change ──")

    r = coin_change_greedy([1, 5, 10, 25], 41)
    check("41¢ → exact change (remainder=0)",  r["remainder"] == 0)
    check("41¢ → uses 4 coins",                r["total_coins"] == 4)   # 25+10+5+1
    check("41¢ → first coin is 25",            r["coins_used"][0][0] == 25)

    r2 = coin_change_greedy([1, 5, 10, 25], 100)
    check("100¢ → 4 quarters",                 r2["total_coins"] == 4)

    r3 = coin_change_greedy([3, 5], 7)
    # greedy: 5+? — 7-5=2, but no coin ≤2; remainder 2
    check("7 with [3,5] → remainder 2 (greedy)",  r3["remainder"] == 2)


# ── huffman coding tests ──────────────────────────────────────────────────────────

def test_huffman() -> None:
    print("\n  ── Huffman Coding ──")

    r = huffman_encode("aabbcc")
    check("aabbcc → codes for a, b, c",     set(r["codes"].keys()) == {"a", "b", "c"})
    check("aabbcc → encoded not empty",     len(r["encoded"]) > 0)
    check("aabbcc → savings ≥ 0%",          r["savings_pct"] >= 0)

    r2 = huffman_encode("aaaa")
    check("single char 'aaaa' → code='0'",  r2["codes"].get("a") == "0")

    r3 = huffman_encode("ab")
    check("'ab' → each code length 1",      all(len(c) == 1 for c in r3["codes"].values()))


# ── fractional knapsack tests ─────────────────────────────────────────────────────

def test_fractional_knapsack() -> None:
    print("\n  ── Fractional Knapsack ──")

    items = [Item("A", 60, 10), Item("B", 100, 20), Item("C", 120, 30)]
    r = fractional_knapsack(items, 50)
    check("capacity=50 → fills exactly",    abs(r["total_weight"] - 50) < 1e-6)
    check("capacity=50 → value=240",        abs(r["total_value"] - 240) < 1e-6)

    items2 = [Item("X", 10, 5)]
    r2 = fractional_knapsack(items2, 3)
    check("partial fill: weight=3 of 5",    abs(r2["total_weight"] - 3) < 1e-6)
    check("partial fill: value=6",          abs(r2["total_value"] - 6) < 1e-6)

    r3 = fractional_knapsack(items, 0)
    check("capacity=0 → value=0",           r3["total_value"] == 0)


# ── job scheduling tests ──────────────────────────────────────────────────────────

def test_job_scheduling() -> None:
    print("\n  ── Job Scheduling ──")

    jobs = [
        Job("J1", deadline=2, profit=100),
        Job("J2", deadline=1, profit=19),
        Job("J3", deadline=2, profit=27),
        Job("J4", deadline=1, profit=25),
        Job("J5", deadline=3, profit=15),
    ]
    r = job_scheduling(jobs)
    scheduled_ids = {j.job_id for _, j in r["scheduled"]}
    check("3 jobs scheduled",               len(r["scheduled"]) == 3)
    check("J1 (highest profit) scheduled",  "J1" in scheduled_ids)
    check("total profit = 142",             abs(r["total_profit"] - 142) < 1e-6)

    single = [Job("S1", deadline=1, profit=50)]
    r2 = job_scheduling(single)
    check("single job → scheduled",         len(r2["scheduled"]) == 1)

    no_slot = [Job("A", 1, 10), Job("B", 1, 20)]
    r3 = job_scheduling(no_slot)
    check("two jobs, one slot → 1 skipped", len(r3["skipped"]) == 1)


# ── runner ────────────────────────────────────────────────────────────────────────

def run_all() -> None:
    print("\n" + "═" * 52)
    print("  GREEDY SUITE — AUTOMATED TEST RUN")
    print("═" * 52)

    test_coin_change()
    test_huffman()
    test_fractional_knapsack()
    test_job_scheduling()

    total  = len(_results)
    passed = sum(1 for _, ok in _results if ok)
    failed = total - passed

    print()
    print("═" * 52)
    print(f"  Results: {passed}/{total} passed", end="")
    if failed:
        print(f"  |  \033[91m{failed} failed\033[0m")
    else:
        print(f"  ✔  \033[92mAll tests passed!\033[0m")
    print("═" * 52 + "\n")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    run_all()
