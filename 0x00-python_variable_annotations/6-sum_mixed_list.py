#!/usr/bin/env python3
'''task 6.
'''
from typing import List, Union


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    '''sums a list of ints and floats.
    '''
    return float(sum(mixed_list))