#!/usr/bin/env python3
"""This module contains a function that returns am asyncio task."""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio task."""
    return asyncio.create_task(wait_random(max_delay))
