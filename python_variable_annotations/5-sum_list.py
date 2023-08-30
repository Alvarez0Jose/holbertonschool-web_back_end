#!/usr/bin/env python3
"""
Module that has function with a list of floats as arguments
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that sum all floats in the list
    """
    result = sum(input_list)

    return result
