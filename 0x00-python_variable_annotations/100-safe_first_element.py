#!/usr/bin/env python3
"""This module contains a duck-typed annotations function"""


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function returns the first element of a sequence or None"""
    if lst:
        return lst[0]
    else:
        return None
