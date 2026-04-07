# Greedy Algorithm Suite  v1.0

A menu-driven Python application that demonstrates four classic **Greedy Algorithms**, built as a group programming project.

---

## Project Structure

```
greedy_suite/
├── main.py                        ← Entry point (run this)
├── menu.py                        ← Member 5 · Menu system & integration
├── algorithms/
│   ├── __init__.py
│   ├── coin_change.py             ← Member 1 · Coin Change Problem
│   ├── huffman_coding.py          ← Member 2 · Huffman Coding
│   ├── fractional_knapsack.py     ← Member 3 · Fractional Knapsack
│   └── job_scheduling.py          ← Member 4 · Job Scheduling with Deadlines
├── utils/
│   ├── __init__.py
│   └── display.py                 ← Shared terminal rendering helpers
└── tests/
    └── test_algorithms.py         ← Member 5 · Automated test suite
```

---

## How to Run

**Requirements:** Python 3.8+  (no third-party packages needed)

```bash
cd greedy_suite
python main.py
```

To run tests:

```bash
python tests/test_algorithms.py
```

---

## Function Allocation

| Function | Algorithm | Greedy Strategy |
|--------|-----------|-----------------|
| Function 1 | Coin Change Problem | Largest denomination first |
| Function 2 | Huffman Coding | Merge lowest-frequency nodes |
| Function 3 | Fractional Knapsack | Highest value/weight ratio |
| Function 4 | Job Scheduling with Deadlines | Highest profit first |
| Function 5 | Menu system, integration & testing | — |

---

## Algorithm Summaries

### 1. Coin Change Problem
Given a set of coin denominations and a target amount, the greedy strategy repeatedly picks the **largest coin that still fits** into the remaining amount. Note: greedy does not always guarantee an optimal solution for arbitrary denomination sets (dynamic programming does), but works perfectly for standard currency systems.

### 2. Huffman Coding
Builds an optimal prefix-free binary encoding by repeatedly **merging the two nodes with the lowest frequencies** using a min-heap. Characters that appear more frequently receive shorter codes, achieving data compression.

### 3. Fractional Knapsack
Given items with values and weights and a knapsack with a weight capacity, the greedy strategy sorts items by **value-to-weight ratio** (highest first) and greedily takes as much of each item as possible. Unlike 0/1 knapsack, fractions of items are allowed.

### 4. Job Scheduling with Deadlines
Given a set of jobs each with a deadline and profit, the greedy strategy processes jobs in **descending profit order** and schedules each into the latest available time slot at or before its deadline, maximising total profit.

---

## References

1. GeeksforGeeks. (2023). *Greedy Algorithm to find Minimum number of Coins.*  
   https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/

2. Programiz. (2023). *Huffman Coding.*  
   https://www.programiz.com/dsa/huffman-coding

3. GeeksforGeeks. (2023). *Fractional Knapsack Problem.*  
   https://www.geeksforgeeks.org/fractional-knapsack-problem/

4. GeeksforGeeks. (2023). *Job Sequencing Problem.*  
   https://www.geeksforgeeks.org/job-sequencing-problem/

> All references were used for **conceptual understanding only**. All source code is original work by the group.
