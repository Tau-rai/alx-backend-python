#!/usr/bin/env python3
"""This module has a type-annotated function"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum elements of a list"""
    sum: float = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return sum
