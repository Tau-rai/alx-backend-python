#!/usr/bin/env python3
"""This module contains a function that returns the length of an element"""


from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples, each containing a sequence and its length"""
    result = []
    for i in lst:
        try:
            result.append((i, len(i)))
        except TypeError:
            print(f"Element {i} is not a sequence.")
    return result
