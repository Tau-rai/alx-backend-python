#!/usr/bin/env python3
"""This module contains a type-annotated function"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up list elements and returns a float"""
    sum: float = 0
    for i in range(len(mxd_lst)):
        sum += mxd_lst[i]
    return sum
