"""
=========================================================
  menu.py  —  Member 5: Menu system, integration & testing
  Orchestrates all four greedy algorithm modules under
  a single interactive terminal interface.
=========================================================
"""

import sys
from utils.display import (
    C, clear, print_banner, section_header,
    divider, pause, warning, success, thinking
)
from algorithms import coin_change, huffman_coding, fractional_knapsack, job_scheduling


# ── menu definitions ─────────────────────────────────────────────────────────────

ALGORITHMS = [
    {
        "key":    "1",
        "label":  "Coin Change Problem",
        "member": "Member 1",
        "module": coin_change,
        "icon":   "🪙",
        "hint":   "Largest denomination first",
    },
    {
        "key":    "2",
        "label":  "Huffman Coding",
        "member": "Member 2",
        "module": huffman_coding,
        "icon":   "🌲",
        "hint":   "Merge lowest-frequency nodes",
    },
    {
        "key":    "3",
        "label":  "Fractional Knapsack",
        "member": "Member 3",
        "module": fractional_knapsack,
        "icon":   "🎒",
        "hint":   "Highest value/weight ratio",
    },
    {
        "key":    "4",
        "label":  "Job Scheduling with Deadlines",
        "member": "Member 4",
        "module": job_scheduling,
        "icon":   "📅",
        "hint":   "Highest profit first",
    },
]


# ── about / references screen ────────────────────────────────────────────────────

REFERENCES = """
  ┌─────────────────────────────────────────────────────────────┐
  │                        REFERENCES                           │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  [1] GeeksforGeeks. (2023). Greedy Algorithm to find        │
  │      Minimum number of Coins.                               │
  │      https://www.geeksforgeeks.org/greedy-algorithm-to-     │
  │      find-minimum-number-of-coins/                          │
  │                                                             │
  │  [2] Programiz. (2023). Huffman Coding.                     │
  │      https://www.programiz.com/dsa/huffman-coding           │
  │                                                             │
  │  [3] GeeksforGeeks. (2023). Fractional Knapsack Problem.    │
  │      https://www.geeksforgeeks.org/fractional-knapsack-     │
  │      problem/                                               │
  │                                                             │
  │  [4] GeeksforGeeks. (2023). Job Sequencing Problem.         │
  │      https://www.geeksforgeeks.org/job-sequencing-problem/  │
  │                                                             │
  │  All references were used for conceptual understanding      │
  │  only. All source code is original work.                    │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
"""

MEMBERS = """
  ┌─────────────────────────────────────────────────────────────┐
  │                      GROUP MEMBERS                          │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  Member 1  —  Coin Change Problem                           │
  │  Member 2  —  Huffman Coding                                │
  │  Member 3  —  Fractional Knapsack                           │
  │  Member 4  —  Job Scheduling with Deadlines                 │
  │  Member 5  —  Menu system, integration & testing            │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
"""


# ── menu renderer ────────────────────────────────────────────────────────────────

def print_main_menu() -> None:
    clear()
    print_banner()

    section_header("MAIN MENU", width=56)

    for algo in ALGORITHMS:
        print(f"  {C.BOLD}{C.CYAN}[{algo['key']}]{C.RESET}  "
              f"{algo['icon']}  {C.BOLD}{algo['label']:<32}{C.RESET}  "
              f"{C.DIM}({algo['hint']}){C.RESET}")
        print(f"       {C.DIM}→ {algo['member']}{C.RESET}")
        print()

    divider(56)
    print(f"  {C.BOLD}{C.YELLOW}[A]{C.RESET}  📋  About & References")
    print(f"  {C.BOLD}{C.RED}[Q]{C.RESET}  ⛔  Quit")
    print()
    divider(56)


# ── about screen ─────────────────────────────────────────────────────────────────

def show_about() -> None:
    clear()
    section_header("ABOUT THIS PROGRAM", width=64)
    print(MEMBERS)
    print(REFERENCES)
    pause()


# ── dispatch ─────────────────────────────────────────────────────────────────────

def dispatch(choice: str) -> None:
    """Route a menu choice to the correct algorithm module."""
    for algo in ALGORITHMS:
        if choice == algo["key"]:
            clear()
            thinking("Initialising", duration=0.5)
            algo["module"].run()
            pause()
            return

    if choice.upper() == "A":
        show_about()
        return

    if choice.upper() == "Q":
        farewell()
        sys.exit(0)

    warning(f"\n  Unknown option: '{choice}'  — please try again.\n")
    pause()


# ── farewell ─────────────────────────────────────────────────────────────────────

def farewell() -> None:
    clear()
    print()
    print(f"{C.CYAN}{C.BOLD}")
    print("  ╔══════════════════════════════════════════╗")
    print("  ║                                          ║")
    print("  ║   Thanks for using Greedy Suite v1.0!   ║")
    print("  ║   Happy coding  ✦                        ║")
    print("  ║                                          ║")
    print("  ╚══════════════════════════════════════════╝")
    print(f"{C.RESET}")


# ── main loop ────────────────────────────────────────────────────────────────────

def main() -> None:
    while True:
        print_main_menu()
        try:
            choice = input(f"  {C.BOLD}Select option ▸{C.RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            farewell()
            sys.exit(0)

        dispatch(choice)
