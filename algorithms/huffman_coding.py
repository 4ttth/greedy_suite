"""
=========================================================
  Member 2 — Huffman Coding
  Greedy Strategy: Merge the two lowest-frequency nodes.
=========================================================

Reference:
  Programiz. (2023). "Huffman Coding."
  https://www.programiz.com/dsa/huffman-coding
  Used for conceptual understanding of tree construction;
  implementation and display logic are original.
"""

import heapq
from utils.display import section_header, divider, success, warning


# ── node definition ──────────────────────────────────────────────────────────────

class HuffNode:
    """A node in the Huffman tree."""

    __slots__ = ("char", "freq", "left", "right")

    def __init__(self, char: str | None, freq: int,
                 left: "HuffNode | None" = None,
                 right: "HuffNode | None" = None):
        self.char  = char
        self.freq  = freq
        self.left  = left
        self.right = right

    # heapq needs comparison; compare by frequency only
    def __lt__(self, other: "HuffNode") -> bool:
        return self.freq < other.freq

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


# ── core algorithm ───────────────────────────────────────────────────────────────

def build_huffman_tree(frequencies: dict[str, int]) -> HuffNode:
    """
    Build a Huffman tree from a character-frequency mapping.
    Uses a min-heap to always merge the two lowest-frequency nodes.
    """
    heap: list[HuffNode] = [HuffNode(ch, fr) for ch, fr in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left  = heapq.heappop(heap)   # lowest freq
        right = heapq.heappop(heap)   # second lowest
        merged = HuffNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]


def _generate_codes(node: HuffNode | None, prefix: str,
                    codes: dict[str, str]) -> None:
    """Recursively generate binary codes via DFS."""
    if node is None:
        return
    if node.is_leaf():
        codes[node.char] = prefix if prefix else "0"   # single-char edge case
        return
    _generate_codes(node.left,  prefix + "0", codes)
    _generate_codes(node.right, prefix + "1", codes)


def huffman_encode(text: str) -> dict:
    """
    Full Huffman encode pipeline.

    Returns a result dict with:
      - frequencies   : char → count
      - codes         : char → binary string
      - encoded       : full encoded binary string
      - original_bits : bit-length of naive 8-bit ASCII encoding
      - encoded_bits  : bit-length of Huffman-encoded string
      - savings_pct   : compression percentage
    """
    if not text:
        return {}

    freq: dict[str, int] = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    root  = build_huffman_tree(freq)
    codes: dict[str, str] = {}
    _generate_codes(root, "", codes)

    encoded       = "".join(codes[ch] for ch in text)
    original_bits = len(text) * 8
    encoded_bits  = len(encoded)
    savings_pct   = (1 - encoded_bits / original_bits) * 100 if original_bits else 0

    return {
        "frequencies":   freq,
        "codes":         codes,
        "encoded":       encoded,
        "original_bits": original_bits,
        "encoded_bits":  encoded_bits,
        "savings_pct":   savings_pct,
        "text":          text,
    }


# ── I/O helpers ──────────────────────────────────────────────────────────────────

def get_input() -> str:
    print()
    print("  Enter a string to encode with Huffman Coding.")
    print("  Example: hello world")
    text = input("  Input string ▸ ").strip()
    return text


def display_result(result: dict) -> None:
    print()
    section_header("HUFFMAN CODING — RESULT", width=60)

    print(f"  Original text  : {result['text']}")
    divider(60)

    print(f"  {'CHAR':^8}  {'FREQ':>6}  {'CODE':<20}  {'CODE LEN':>8}")
    divider(60)

    sorted_codes = sorted(result["codes"].items(),
                          key=lambda kv: result["frequencies"][kv[0]], reverse=True)
    for ch, code in sorted_codes:
        display_ch = repr(ch) if ch == " " else ch
        freq       = result["frequencies"][ch]
        print(f"  {display_ch:^8}  {freq:>6}  {code:<20}  {len(code):>8}")

    divider(60)
    print(f"  Original size (8-bit ASCII) : {result['original_bits']} bits")
    print(f"  Huffman encoded size        : {result['encoded_bits']} bits")
    success(f"  Compression saving          : {result['savings_pct']:.1f}%")

    # Show encoded output (truncated for readability)
    encoded_preview = result["encoded"]
    if len(encoded_preview) > 64:
        encoded_preview = encoded_preview[:64] + "…"
    print(f"\n  Encoded bits ▸  {encoded_preview}")
    print()


# ── entry point ──────────────────────────────────────────────────────────────────

def run() -> None:
    section_header("HUFFMAN CODING", width=60)
    print("  Strategy : merge the two lowest-frequency nodes (greedy)")
    print()

    try:
        text = get_input()
        if not text:
            warning("  Input cannot be empty.")
            return
        result = huffman_encode(text)
        display_result(result)
    except Exception as exc:
        warning(f"  Error: {exc}")
