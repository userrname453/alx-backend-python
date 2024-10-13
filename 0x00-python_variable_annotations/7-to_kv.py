#!/usr/bin/env python3
'''task 7.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple with k=k and value = value^2.
    '''
    return (k, float(v**2))