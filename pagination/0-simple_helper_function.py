#!/usr/bin/env python3
"""
Module that returns a start and end index for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that calculates the start and end of the index
    """

    end_size: int = page * page_size
    start_size: int = end_size - page_size

    return (start_size, end_size)
