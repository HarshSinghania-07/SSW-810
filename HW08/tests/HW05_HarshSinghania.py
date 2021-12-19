'''

NAME: HARSH SINGHANIA 
SSW 810 - HW05
CWID - 20007289
This homework has 4 parts - String methods, Slices, Working with files 
and Automated Testing.

'''

from typing import List, Iterator
from pathlib import Path
import os.path

def reverse(s: str) -> str:
    """Reversing the string."""
    if type(s) != str:
        raise TypeError("Value must be a str")

    result = ''
    for i in range(len(s)-1, -1, -1):
        result = result + s[i]
    return(result)

def find_second(target: str, sequence: str) -> int:
    """Used to return the second occurence of the target in the sequence"""

    return find_nth_occurrence(target, sequence, 2)

def find_nth_occurrence(target: str,
                        word: str,
                        occurrence_position: int = 1) -> int:
    """Find the nth position for the occurrence for the target word"""

    if type(target) != str:
        raise TypeError("Value must be a str")
    if type(word) != str:
        raise TypeError("Value must be a str")
    if type(occurrence_position) != int:
        raise TypeError("Value must be an int")
    if occurrence_position < 1:
        raise ValueError('Occurrence must be bigger or equal than one')
    if len(target) > len(word):
        return -1
    if len(target) == len(word):
        if target == word:
            return 0
        return -1

    founds: List[int] = []
    for offset in range(len(word) - len(target) + 1):
        substr: str = word[offset:(len(target) + offset)]
        if substr == target:
            founds.append(offset)

    for index, offset in enumerate(founds):
        if index + 1 == occurrence_position:
            return offset
    return -1

def substring(target: str, word: str) -> int:
    """Returns the first offset from the beginning of string word
     where target occurs in word."""

    return find_nth_occurrence(target, word)

def remove_comments(line: str) -> str:
    """Receives a string to remove the comments"""

    if len(line) == 0:
        return line

    comment_index = find_nth_occurrence('#', line)
    if comment_index < 0:
        return line.rstrip('\n')
    if comment_index == 0:
        return ''

    response: str = line[0:comment_index]
    return response.rstrip('\n')


def get_lines(path: str) -> Iterator[str]:
    """Find the n position for the occurrence for the target word"""

    if type(path) != str:
        raise TypeError("Value must be a str")
    if not os.path.exists(path):
        raise FileNotFoundError(f'the path {path} do not exist')
    file_path = Path(path)
    if not file_path.is_file():
        raise IOError(f'the path {path} is not a file')

    response: str = ''
    is_continuation: bool = False
    with open(path, "r") as file:
        for line in file.readlines():
            line = line.strip('\n')
            if len(line) == 0:
                if is_continuation:
                    response += line
                else:
                    yield ''
                    is_continuation = False
                    continue
            if line[-1] == '\\':
                line = line.rstrip('\\')
                response += line
                is_continuation = True
                continue

            is_continuation = False
            response += line
            response = remove_comments(response)
            if len(response) > 0:
                yield response
                response = ''

        if len(response) > 0 and is_continuation:
            yield response
        file.close()