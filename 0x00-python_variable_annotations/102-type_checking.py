#!/usr/bin/env python3
"""This module contains the type_checking function"""


from typing import List, Tuple, Union


def zoom_array(lst: Union[Tuple, List], factor: Union[int, float] = 2) -> List:
    """Zooms in on an array"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
