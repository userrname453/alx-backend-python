#!/usr/bin/env python3
'''task 12.
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''creates copies of the items in the tuple.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
print(zoom_2x)
zoom_3x = zoom_array(array, 3)
print(zoom_3x)