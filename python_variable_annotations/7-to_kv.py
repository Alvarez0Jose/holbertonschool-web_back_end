#!/usr/bin/env python3
"""
Module that returns a tuple[str, float]
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that returns a tuple
    """
    return tuple([k, v * v])
