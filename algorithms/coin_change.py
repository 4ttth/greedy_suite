"""
=========================================================
  Member 1 — Coin Change Problem
  Greedy Strategy: Choose the largest denomination first.
=========================================================

Reference:
  GeeksforGeeks. (2023). "Greedy Algorithm to find Minimum number of Coins."
  https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
  Used for conceptual understanding; implementation is original.
"""

from utils.display import section_header, row, divider, success, warning


# ── core algorithm ──────────────────────────────────────────────────────────────

def coin_change_greedy(denominations: list[int], amount: int) -> dict:
    """
    Greedily selects the largest available coin that fits into the remaining
    amount, repeating until the amount is exhausted or no coin fits.

    Returns a result dict with:
      - coins_used   : list of (denomination, count) pairs
      - total_coins  : total number of coins used
      - remainder    : leftover amount (0 means exact change was made)
      - steps        : step-by-step trace for display
    """
    sorted_denoms = sorted(denominations, reverse=True)
    remaining     = amount
    coins_used    = []
    steps         = []

    for coin in sorted_denoms:
        if remaining <= 0:
            break
        count = remaining // coin
        if count > 0:
            coins_used.append((coin, count))
            steps.append({
                "coin":      coin,
                "count":     count,
                "subtracted": coin * count,
                "remaining": remaining - coin * count,
            })
            remaining -= coin * count

    return {
        "coins_used":  coins_used,
        "total_coins": sum(c for _, c in coins_used),
        "remainder":   remaining,
        "steps":       steps,
        "amount":      amount,
        "denoms":      sorted_denoms,
    }


# ── I/O helpers ─────────────────────────────────────────────────────────────────

def get_input() -> tuple[list[int], int]:
    """Prompt user for denominations and target amount."""
    print()
    print("  Enter coin denominations separated by spaces.")
    print("  Example: 1 5 10 25  (for US cents)")
    raw = input("  Denominations ▸ ").strip()
    denominations = sorted(set(int(x) for x in raw.split()), reverse=True)

    print()
    raw_amount = input("  Target amount ▸ ").strip()
    amount = int(raw_amount)

    return denominations, amount


def display_result(result: dict) -> None:
    """Render the coin-change result in a formatted table."""
    print()
    section_header("COIN CHANGE — RESULT", width=54)

    print(f"  Target amount  : {result['amount']}")
    print(f"  Denominations  : {result['denoms']}")
    divider(54)

    if not result["steps"]:
        warning("  No coins could be applied.")
        return

    print(f"  {'COIN':>8}   {'COUNT':>6}   {'SUBTRACTED':>12}   {'REMAINING':>10}")
    divider(54)
    for s in result["steps"]:
        print(f"  {s['coin']:>8}   {s['count']:>6}   {s['subtracted']:>12}   {s['remaining']:>10}")
    divider(54)

    print(f"  Total coins used : {result['total_coins']}")

    if result["remainder"] == 0:
        success("  ✔  Exact change achieved!")
    else:
        warning(f"  ⚠  Remainder: {result['remainder']} (greedy cannot make exact change)")

    print()


# ── entry point called by menu ───────────────────────────────────────────────────

def run() -> None:
    section_header("COIN CHANGE PROBLEM", width=54)
    print("  Strategy : largest denomination first (greedy)")
    print()

    try:
        denominations, amount = get_input()
        if amount <= 0:
            warning("  Amount must be a positive integer.")
            return
        result = coin_change_greedy(denominations, amount)
        display_result(result)
    except ValueError:
        warning("  Invalid input — please enter integers only.")
