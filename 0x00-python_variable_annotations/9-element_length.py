#!/usr/bin/env python3
"""This module contains a function that returns the length of an element"""


from typing import Sequence, Tuple, List


def element_length(lst: Sequence[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples, each containing a sequence and its length"""
    return [(i, len(i)) for i in lst]
