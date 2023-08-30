#!/usr/bin/env python3
"""
Module that returns the type of all
arguments in the function
"""
from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that return a list with a tuple
    """
    return [(i, len(i)) for i in lst]
