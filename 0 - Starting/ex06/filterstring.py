#!/usr/bin/env python3
"""
filterstring.py
Takes a string S and an integer N, and prints the list of words from S
whose length is greater than N.
"""

import sys
from ft_filter import ft_filter


def main() -> None:
    """
    Main entry point.
    Validates arguments, applies ft_filter with a lambda and a
        list comprehension.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        s_arg = sys.argv[1]
        n_arg = sys.argv[2]

        try:
            n = int(n_arg)
        except ValueError:
            raise AssertionError("the arguments are bad")

        if not isinstance(s_arg, str):
            raise AssertionError("the arguments are bad")

        words = s_arg.split()

        result = [word for word in ft_filter(lambda w: len(w) > n, words)]

        print(result)

    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
