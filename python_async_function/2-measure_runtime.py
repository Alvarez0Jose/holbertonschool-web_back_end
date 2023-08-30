#!/usr/bin/env python3
"""
Module that returns total execution time
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Funtion that calculates the time of execution
    """
    start = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
