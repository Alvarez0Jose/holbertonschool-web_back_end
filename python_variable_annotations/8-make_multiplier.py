#!/usr/bin/env python3
"""
Module that takes a float as argument and returns
a function that multiplies said float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and returns a function that multiplies
    a float by the given multiplier
    """
    def multiplier_function(d: float) -> float:
        return d * multiplier
    
    return multiplier_function
