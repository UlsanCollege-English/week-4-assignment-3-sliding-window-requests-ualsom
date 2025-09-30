[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/N1lYjCLq)
se the same workflow as HW1)

3) hw3-rate-limiter/ — Sliding-Window Requests (Queue of Timestamps)
README.md
# HW3 — API Rate Limiter (Sliding Window)

## Story
You’re protecting a tiny API from spikes. The rule: allow at most **N requests** in the **last W seconds** for each client.

## Task (Technical)
Implement `RateLimiter(N, W)` with:
- `allow(t: int) -> bool`: if accepting a request at unix time `t` keeps the last-`W` second **window** at ≤ `N`, return `True` and record it; else return `False`.
- Sliding window is **(t - W, t]** (strictly greater than `t-W`, up to `t` inclusive).

Use a **queue of timestamps** and evict stale entries each call.

## Hints
1) Before evaluating, **pop left** while `queue[0] <= t - W`.
2) Compare `len(queue)` with `N` to allow/deny.
3) Append `t` only on allow.

## Run tests locally
```bash
python -m pytest -q
```
## Subimission

Push to GitHub Classroom

Commit → push → check Actions.

## Common problems

- Off-by-one on the window bounds.

- Forgetting to evict before counting.