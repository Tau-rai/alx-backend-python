#!/usr/bin/env python3
"""This module contains concurrent coroutines."""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function returns the list of all the delays"""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
