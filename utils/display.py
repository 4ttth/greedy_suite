"""
=========================================================
  utils/display.py
  Shared terminal-rendering helpers used by all modules.
=========================================================
"""

import os
import sys
import time


# ── ANSI palette ─────────────────────────────────────────────────────────────────

class C:
    """ANSI colour/style codes.  Auto-stripped if stdout is not a tty."""
    _tty = sys.stdout.isatty()

    RESET    = "\033[0m"   if _tty else ""
    BOLD     = "\033[1m"   if _tty else ""
    DIM      = "\033[2m"   if _tty else ""

    # foreground
    BLACK    = "\033[30m"  if _tty else ""
    RED      = "\033[91m"  if _tty else ""
    GREEN    = "\033[92m"  if _tty else ""
    YELLOW   = "\033[93m"  if _tty else ""
    BLUE     = "\033[94m"  if _tty else ""
    MAGENTA  = "\033[95m"  if _tty else ""
    CYAN     = "\033[96m"  if _tty else ""
    WHITE    = "\033[97m"  if _tty else ""

    # background
    BG_BLACK  = "\033[40m" if _tty else ""
    BG_BLUE   = "\033[44m" if _tty else ""
    BG_CYAN   = "\033[46m" if _tty else ""


# ── primitives ────────────────────────────────────────────────────────────────────

def divider(width: int = 56, char: str = "─") -> None:
    print(f"  {C.DIM}{char * width}{C.RESET}")


def section_header(title: str, width: int = 56) -> None:
    """Render a highlighted section header."""
    pad   = max(0, width - len(title) - 2)
    left  = pad // 2
    right = pad - left
    bar   = "─" * width
    print()
    print(f"  {C.CYAN}{C.BOLD}╔{bar}╗{C.RESET}")
    print(f"  {C.CYAN}{C.BOLD}║{' ' * left}{title}{' ' * right}║{C.RESET}")
    print(f"  {C.CYAN}{C.BOLD}╚{bar}╝{C.RESET}")
    print()


def row(label: str, value: str, width: int = 30) -> None:
    print(f"  {C.DIM}{label:<{width}}{C.RESET}  {value}")


def success(msg: str) -> None:
    print(f"{C.GREEN}{msg}{C.RESET}")


def warning(msg: str) -> None:
    print(f"{C.YELLOW}{msg}{C.RESET}")


def error(msg: str) -> None:
    print(f"{C.RED}{msg}{C.RESET}")


# ── splash / banner ───────────────────────────────────────────────────────────────

BANNER = rf"""
{C.CYAN}{C.BOLD}
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║    ██████  ██████  ███████ ███████ ██████  ██    ██     ║
  ║   ██       ██   ██ ██      ██      ██   ██  ██  ██      ║
  ║   ██   ███ ██████  █████   █████   ██   ██   ████       ║
  ║   ██    ██ ██   ██ ██      ██      ██   ██    ██        ║
  ║    ██████  ██   ██ ███████ ███████ ██████     ██        ║
  ║                                                          ║
  ║          A L G O R I T H M   S U I T E  v1.0            ║
  ╚══════════════════════════════════════════════════════════╝
{C.RESET}"""


def print_banner() -> None:
    print(BANNER)
    tagline = "  Classic Greedy Algorithms — Interactive Python Playground"
    print(f"{C.DIM}{tagline}{C.RESET}\n")


# ── "press enter" prompt ──────────────────────────────────────────────────────────

def pause() -> None:
    print()
    input(f"  {C.DIM}Press Enter to return to menu…{C.RESET}")


# ── clear screen (cross-platform) ────────────────────────────────────────────────

def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


# ── animated "thinking" indicator ────────────────────────────────────────────────

def thinking(msg: str = "Computing", duration: float = 0.6) -> None:
    """Brief animated dot-dot-dot indicator."""
    if not sys.stdout.isatty():
        return
    frames  = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end     = time.time() + duration
    idx     = 0
    while time.time() < end:
        print(f"\r  {C.CYAN}{frames[idx % len(frames)]}{C.RESET}  {msg}…",
              end="", flush=True)
        time.sleep(0.08)
        idx += 1
    print("\r" + " " * (len(msg) + 12) + "\r", end="", flush=True)
