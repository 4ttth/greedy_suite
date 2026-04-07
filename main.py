#!/usr/bin/env python3
"""
=========================================================
  main.py — Entry Point
  Greedy Algorithm Suite  |  v1.0
=========================================================
  Run this file to launch the interactive menu.
  Requires Python 3.10+  (uses match/case in Python ≥3.10,
  but this project uses plain if/elif for compatibility).
=========================================================

  Usage:
      python main.py
=========================================================
"""

import sys
import os

# Ensure the project root is on sys.path regardless of the
# working directory the user launches the script from.
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from menu import main

if __name__ == "__main__":
    main()
