#!/usr/bin/env python3
"""
Module that returns the list of all the delays
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that returns a list of floats in ascending order
    """
    delay_list: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delay_list.append(delay)

    return delay_list