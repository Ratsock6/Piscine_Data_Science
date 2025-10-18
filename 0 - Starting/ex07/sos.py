#!/usr/bin/env python3
"""
sos.py
Encode a given string (alphanumeric + spaces) into Morse code.

Rules:
- Alphanumeric characters map to dots (.) and dashes (-).
- Complete Morse characters are separated by a single space.
- Space characters are represented by a slash (/).
"""

import sys


MORSE: dict[str, str] = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/",
}


def encode_morse(text: str) -> str:
    """
    Encode a text (alphanumeric + spaces) into Morse.

    Args:
        text (str): Input text to encode.

    Returns:
        str: Morse-encoded string with single spaces between codes.

    Raises:
        AssertionError: If text contains characters outside allowed set.
    """
    allowed = set(MORSE.keys())
    chars = list(text.upper())
    if not all(c in allowed for c in chars):
        raise AssertionError("the arguments are bad")
    return " ".join(MORSE[c] for c in chars)


def main() -> None:
    """
    Parse CLI args, validate, encode to Morse, and print the result.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        arg = sys.argv[1]
        if not isinstance(arg, str):
            raise AssertionError("the arguments are bad")
        print(encode_morse(arg))
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
