#!/usr/bin/env python3
'''task 9.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(my_list: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a list containing tuple (el,lenth).
    '''
    return [(i, len(i)) for i in my_list]
