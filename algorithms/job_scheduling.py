"""
=========================================================
  Member 4 — Job Scheduling with Deadlines
  Greedy Strategy: Highest profit job first; fit each
                   job into the latest free slot ≤ its
                   deadline.
=========================================================

Reference:
  GeeksforGeeks. (2023). "Job Sequencing Problem."
  https://www.geeksforgeeks.org/job-sequencing-problem/
  Used for conceptual understanding; implementation is original.
"""

from utils.display import section_header, divider, success, warning


# ── data model ───────────────────────────────────────────────────────────────────

class Job:
    """Represents a schedulable job."""

    def __init__(self, job_id: str, deadline: int, profit: float):
        self.job_id   = job_id
        self.deadline = deadline
        self.profit   = profit

    def __repr__(self) -> str:
        return f"Job({self.job_id!r}, deadline={self.deadline}, profit={self.profit})"


# ── core algorithm ───────────────────────────────────────────────────────────────

def job_scheduling(jobs: list[Job]) -> dict:
    """
    Greedy job scheduling: sort by profit descending, then slot
    each job into the latest available time slot ≤ its deadline.

    Runs in O(n²) using a slot array.

    Returns a result dict with:
      - scheduled     : list of (slot, job) in slot order
      - skipped       : jobs that could not be scheduled
      - total_profit  : sum of scheduled job profits
      - max_deadline  : horizon used for the slot array
    """
    sorted_jobs = sorted(jobs, key=lambda j: j.profit, reverse=True)
    max_deadline = max(j.deadline for j in jobs) if jobs else 0

    # slot[t] = Job assigned to time slot t (1-indexed), or None
    slots: list[Job | None] = [None] * (max_deadline + 1)

    scheduled = []
    skipped   = []

    for job in sorted_jobs:
        # Try to place in latest free slot ≤ deadline
        placed = False
        for t in range(min(job.deadline, max_deadline), 0, -1):
            if slots[t] is None:
                slots[t]  = job
                scheduled.append((t, job))
                placed = True
                break
        if not placed:
            skipped.append(job)

    scheduled.sort(key=lambda x: x[0])   # order by time slot
    total_profit = sum(j.profit for _, j in scheduled)

    return {
        "scheduled":    scheduled,
        "skipped":      skipped,
        "total_profit": total_profit,
        "max_deadline": max_deadline,
        "sorted_jobs":  sorted_jobs,
    }


# ── I/O helpers ──────────────────────────────────────────────────────────────────

def get_input() -> list[Job]:
    print()
    print("  How many jobs do you want to schedule?")
    n = int(input("  Number of jobs ▸ ").strip())

    jobs = []
    print()
    for i in range(1, n + 1):
        print(f"  — Job {i} —")
        job_id   = input(f"    Job ID   ▸ ").strip() or f"J{i}"
        deadline = int(input(f"    Deadline ▸ ").strip())
        profit   = float(input(f"    Profit   ▸ ").strip())
        jobs.append(Job(job_id, deadline, profit))
        print()

    return jobs


def display_result(result: dict) -> None:
    print()
    section_header("JOB SCHEDULING — RESULT", width=58)

    # Jobs sorted by profit for reference
    print("  Jobs sorted by profit (greedy order):")
    divider(58)
    print(f"  {'JOB ID':<10}  {'DEADLINE':>8}  {'PROFIT':>10}  {'STATUS':<10}")
    divider(58)

    sched_ids = {j.job_id for _, j in result["scheduled"]}
    for job in result["sorted_jobs"]:
        status = "✔ Scheduled" if job.job_id in sched_ids else "✘ Skipped"
        print(f"  {job.job_id:<10}  {job.deadline:>8}  {job.profit:>10.2f}  {status:<10}")

    divider(58)
    print("\n  Scheduled sequence (by time slot):")
    divider(58)
    print(f"  {'SLOT':>6}  {'JOB ID':<10}  {'DEADLINE':>8}  {'PROFIT':>10}")
    divider(58)
    for slot, job in result["scheduled"]:
        print(f"  {slot:>6}  {job.job_id:<10}  {job.deadline:>8}  {job.profit:>10.2f}")

    divider(58)
    success(f"  Total profit : {result['total_profit']:.2f}")
    if result["skipped"]:
        warning(f"  Skipped jobs : {', '.join(j.job_id for j in result['skipped'])}")
    print()


# ── entry point ──────────────────────────────────────────────────────────────────

def run() -> None:
    section_header("JOB SCHEDULING WITH DEADLINES", width=58)
    print("  Strategy : highest profit first; latest available slot (greedy)")
    print()

    try:
        jobs = get_input()
        if not jobs:
            warning("  No jobs provided.")
            return
        result = job_scheduling(jobs)
        display_result(result)
    except ValueError:
        warning("  Invalid input — please enter correct data types.")
