#!/usr/bin/env python3
"""This module contains the type_checking function"""


from typing import List


def zoom_array(lst: List[int], factor: float = 2) -> List[int]:
    """Zooms in on an array"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
