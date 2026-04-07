"""
=========================================================
  Member 3 — Fractional Knapsack
  Greedy Strategy: Highest value-to-weight ratio first.
=========================================================

Reference:
  GeeksforGeeks. (2023). "Fractional Knapsack Problem."
  https://www.geeksforgeeks.org/fractional-knapsack-problem/
  Used for conceptual reference; implementation is original.
"""

from utils.display import section_header, divider, success, warning


# ── data model ───────────────────────────────────────────────────────────────────

class Item:
    """Represents a single knapsack item."""

    def __init__(self, name: str, value: float, weight: float):
        self.name    = name
        self.value   = value
        self.weight  = weight
        self.ratio   = value / weight if weight > 0 else 0.0

    def __repr__(self) -> str:
        return f"Item({self.name!r}, v={self.value}, w={self.weight})"


# ── core algorithm ───────────────────────────────────────────────────────────────

def fractional_knapsack(items: list[Item], capacity: float) -> dict:
    """
    Greedily fills the knapsack by taking fractions of the highest
    value/weight ratio items first.

    Returns a result dict with:
      - selected  : list of (item, fraction_taken, value_gained)
      - total_value  : maximum achievable value
      - total_weight : weight used (≤ capacity)
      - steps     : step-by-step trace
    """
    sorted_items = sorted(items, key=lambda i: i.ratio, reverse=True)
    remaining    = capacity
    selected     = []
    steps        = []
    total_value  = 0.0

    for item in sorted_items:
        if remaining <= 0:
            break
        fraction = min(1.0, remaining / item.weight)
        gained   = fraction * item.value
        selected.append((item, fraction, gained))
        steps.append({
            "name":     item.name,
            "ratio":    item.ratio,
            "fraction": fraction,
            "weight":   fraction * item.weight,
            "value":    gained,
        })
        remaining    -= fraction * item.weight
        total_value  += gained

    return {
        "selected":     selected,
        "total_value":  total_value,
        "total_weight": capacity - remaining,
        "capacity":     capacity,
        "steps":        steps,
        "items":        sorted_items,
    }


# ── I/O helpers ──────────────────────────────────────────────────────────────────

def get_input() -> tuple[list[Item], float]:
    print()
    print("  How many items do you want to add?")
    n = int(input("  Number of items ▸ ").strip())

    items = []
    print()
    for i in range(1, n + 1):
        print(f"  — Item {i} —")
        name   = input(f"    Name   ▸ ").strip() or f"Item{i}"
        value  = float(input(f"    Value  ▸ ").strip())
        weight = float(input(f"    Weight ▸ ").strip())
        items.append(Item(name, value, weight))
        print()

    capacity = float(input("  Knapsack capacity ▸ ").strip())
    return items, capacity


def display_result(result: dict) -> None:
    print()
    section_header("FRACTIONAL KNAPSACK — RESULT", width=68)
    print(f"  Capacity : {result['capacity']}")
    divider(68)

    print(f"  {'ITEM':<12}  {'RATIO':>8}  {'FRACTION':>10}  "
          f"{'WEIGHT USED':>12}  {'VALUE GAINED':>13}")
    divider(68)

    for s in result["steps"]:
        frac_pct = f"{s['fraction']*100:.1f}%"
        print(f"  {s['name']:<12}  {s['ratio']:>8.4f}  {frac_pct:>10}  "
              f"  {s['weight']:>10.2f}  {s['value']:>13.2f}")

    divider(68)
    print(f"  Total weight used : {result['total_weight']:.2f} / {result['capacity']}")
    success(f"  Maximum value     : {result['total_value']:.4f}")
    print()


# ── entry point ──────────────────────────────────────────────────────────────────

def run() -> None:
    section_header("FRACTIONAL KNAPSACK", width=68)
    print("  Strategy : highest value/weight ratio first (greedy)")
    print()

    try:
        items, capacity = get_input()
        if not items:
            warning("  No items provided.")
            return
        if capacity <= 0:
            warning("  Capacity must be positive.")
            return
        result = fractional_knapsack(items, capacity)
        display_result(result)
    except ValueError:
        warning("  Invalid input — please enter numeric values.")
