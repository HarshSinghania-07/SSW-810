'''

NAME: HARSH SINGHANIA
SSW 810 - HW04 
CWID- 20007289
In this file, we have 3 functions - Counting vowels, Finding last occurence and
Enumerate.

'''

import unittest
from typing import Sequence, Any, Optional, Iterator


def count_vowels(s) -> int:
    """Function to count the vowels in the sequence"""
    s: str = s.lower()
    counter: int = 0
    for x in s:
        if(x in ['a','e','i','o','u']):
            counter+=1
    
    return counter

def last_occurrence(target, sequence) -> Optional[int]:
    """Function to return the last occurence of the target in the sequence"""
    counter: int =0
    if target not in sequence:
        return None
    for x in sequence:
        if x == target:
            result = counter
        counter+=1
    return result

def my_enumerate(seq) -> Iterator[int]:   
    """This function emulates the enumerate function"""
    counter: int = 0   
    for k in seq:
        yield(counter,k)
        counter+=1