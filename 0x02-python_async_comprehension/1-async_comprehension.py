#!/usr/bin/env python3
"""This module contains an async comprehension function"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This function collects 10 random numbers using an async generator"""
    return [i async for i in async_generator()]
