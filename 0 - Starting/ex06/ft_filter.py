#!/usr/bin/env python3
"""
ft_filter.py
Reimplementation of the built-in filter() function using list comprehensions.
"""

from typing import Callable, Iterable, Iterator


def ft_filter(function: Callable | None, iterable: Iterable) -> Iterator:
    """
    Reimplementation of filter(function or None, iterable).
    Returns an iterator yielding those items of iterable for which
        function(item)
    is true. If function is None, returns the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
