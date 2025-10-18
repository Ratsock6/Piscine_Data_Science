#!/usr/bin/env python3
"""
Loading.py
Reimplements a minimal tqdm-like progress bar using a generator with yield.

Usage pattern (see tester.py):
    from time import sleep
    from Loading import ft_tqdm

    for _ in ft_tqdm(range(333)):
        sleep(0.005)
    print()
"""

from typing import Iterable, Iterator


def ft_tqdm(lst: range) -> Iterator[int]:
    """
    A minimal tqdm-like progress bar implemented with a generator.

    Iterates over `lst`, yields each element, and prints a single-line
    progress bar that updates in place, of the form:
        XX%|[=====>.................]| i/n

    Args:
        lst (range): The range (or any sized iterable) to iterate over.

    Yields:
        int: Each element from `lst`, in order.

    Notes:
        - No timing or ETA to stay within the “Allowed functions: None” spirit.
        - Uses carriage return to rewrite the same line.
        - Final newline is expected to be printed by the caller (see tester.py).
    """
    total = len(lst) if hasattr(lst, "__len__") else 0
    if total == 0:
        return
        yield

    bar_width = 60
    for idx, item in enumerate(lst, start=1):
        ratio = idx / total
        percent = int(ratio * 100)

        filled = int(ratio * bar_width)
        if filled <= 0:
            bar = " " * bar_width
        elif filled >= bar_width:
            bar = "=" * (bar_width - 1) + ">"
        else:
            bar = "=" * (filled - 1) + ">" + " " * (bar_width - filled)

        line = f"\r{percent:3d}%|[{bar}]| {idx}/{total}"
        print(line, end="", flush=True)

        yield item
