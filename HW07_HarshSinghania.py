'''

Author - Harsh Singhania
CWID - 20007289
SSW 810 - HW07
Part 1 - Anagrams
Part 1.2 - Anagrams using dictionaries
Part 1.3 - Anagrams using Counter
Part 2 - Covers Alphabets
Part 3 - Web Analyzer

'''
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set

def anagrams_lst(str1: str, str2: str) -> bool:
    """Function for checking Anagrams."""
    if type(str1)!= str or type(str2) != str:
        raise TypeError("Please enter string only.")
    if len(str1) == 0 or len(str2) ==0:
        raise ValueError("Please enter non empty strings.")
    return (sorted(list(str1)) == sorted(list(str2)))

def anagrams_dd(str1: str, str2: str) -> bool:
    """Function for checking Anagrams using Defaultdict."""
    dd: Dict[str, int] = defaultdict(int)
    for char in str1:
        dd[char] = dd.get(char, 0) + 1
    for char in str2:
        dd[char] = dd.get(char, 0) - 1
    for char in dd.keys():
        if dd.get(char) != 0:
            return False
    return True

def anagrams_cntr(str1: str, str2: str):
    """Checking for Anagrams using counter."""
    return Counter(str1) == Counter(str2)

def covers_alphabet(sentence: str) -> bool:
    """Returns True if sentence includes at least one instance of every
    character in the alphabet or False using only Python sets"""
    return set("".join(filter(str.isalpha,
                              sentence.lower().replace(" ", "")))) == \
           set("abcdefghijklmnopqrstuvwxyz")

def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """Create a summary of the weblogs with each distinct site and a sorted
    list of names of distinct people who visited that site"""
    records: Dict[str, Set] = defaultdict(set)
    list(map(lambda log: records[log[1]].add(log[0]), weblogs))
    return [(w, sorted(list(e))) for w, e in sorted(records.items())]
    