#!/usr/bin/env python3
"""
building.py
Counts character categories in a given text (upper, lower, punctuation, spaces,
digits) and prints a formatted summary.

Usage:
    python building.py "Your text here"
    python building.py            # will prompt and read one line from stdin
"""

import sys


def analyze_text(text: str) -> dict:
    """
    Analyze a text and count character categories.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary with keys:
              'total', 'upper', 'lower', 'punct', 'spaces', 'digits'.
    """
    total = len(text)
    upper = sum(ch.isupper() for ch in text)
    lower = sum(ch.islower() for ch in text)
    digits = sum(ch.isdigit() for ch in text)
    spaces = sum(ch.isspace() for ch in text)
    punct = sum(1 for ch in text if not ch.isalnum() and not ch.isspace())
    return {
        "total": total,
        "upper": upper,
        "lower": lower,
        "punct": punct,
        "spaces": spaces,
        "digits": digits,
    }


def print_report(stats: dict) -> None:
    """
    Print the formatted report given the computed stats.

    Args:
        stats (dict): Counts returned by analyze_text().
    """
    print(f"The text contains {stats['total']} characters:")
    print(f"{stats['upper']} upper letters")
    print(f"{stats['lower']} lower letters")
    print(f"{stats['punct']} punctuation marks")
    print(f"{stats['spaces']} spaces")
    print(f"{stats['digits']} digits")


def main() -> None:
    """
    Entry point: handle args, prompt if needed, validate, and print counts.
    """
    try:
        argc = len(sys.argv)
        if argc > 2:
            raise AssertionError("more than one argument is provided")

        if argc == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()
            if text == "":
                text = ""

        stats = analyze_text(text)
        print_report(stats)

    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
