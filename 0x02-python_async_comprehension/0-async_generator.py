#!/usr/bin/env python3
"""This module caontains an async generator function"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This function returns a random number between 0 and 10"""
    try:
        for _ in range(10):
            await asyncio.sleep(1)
            yield random.uniform(0, 10)
    except Exception as e:
        pass
