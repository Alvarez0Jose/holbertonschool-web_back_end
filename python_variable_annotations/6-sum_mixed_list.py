#!/usr/bin/env python3
"""
Module that sums a list of floats and ints
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Function that sums all int and float of the list
    """
    result = float(sum(mxd_list))
    return result
