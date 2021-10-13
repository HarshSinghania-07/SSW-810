'''

Author - Harsh Singhania
CWID - 20007289
SSW 810 - HW 06
In this homework we work with - Lists & Queue.
Part 1 - Returning a copy of a list using list comprehensions
Part 2 - Finding List Intersect[Common values between 2 lists] using list comprehension
Part 3 - Finding List Difference[Different values between 2 lists] using list comprehension
Part 4 - Removing words that starts with a vowel from a given string
Part 5 - Password Checker function
Part 6 - Creating class Donut Queue for tracking customers visiting a donut shop

'''

from typing import List, Any, Optional

def list_copy(l: List[Any]) -> List[Any]:
    """Functions receives a list and returns a copy"""
    if not isinstance(l, List):
        raise TypeError("input_list is not instance of List")
    return [item for item in l]

def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    """Receives two list and return a new list with the intersected values"""
    if not isinstance(l1, List):
        raise TypeError("first_list is not instance of List")
    if not isinstance(l2, List):
        raise TypeError("second_list is not instance of List")

    combined_list: List[Any] = list(set(l1) | set(l2))
    return [item for item in combined_list if item in l1 and item in l2]

def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    if not isinstance(l1, List):
        raise TypeError("First List is not instance of List")
    if not isinstance(l2, List):
        raise TypeError("Second List is not instance of List")
    return [item for item in l1 if item not in l2]

def remove_vowels(s: str) -> str:
    if type(s) != str:
        raise TypeError("string must be a str")
    vowels: List[str] = ["a", "e", "i", "o", "u"]
    words: List[str] = s.split()

    return ' '.join([word for word in words if word[0].lower() not in vowels])

def check_pwd(password: str) -> bool:
    if type(password) != str:
        raise TypeError("password must be a str")
    if len(password) < 4:
        return False
    if not password[0].isdigit():
        return False
    if len([letter for letter in password if letter.isupper()]) < 2:
        return False
    if len([letter for letter in password if letter.islower()]) < 1:
        return False
    return True

class Customer:
    """Represents a costumer in the Donut queue."""
    __slots__ = ['name', 'vip']
    def __init__(self, name: str, vip: bool = False):
        if type(name) != str:
            raise TypeError("name must be a str")
        if len(name) == 0:
            raise ValueError("name can't be empty")
        if type(vip) != bool:
            raise TypeError("vip must be a bool")
        self.name = name
        self.vip = vip

class DonutQueue:
    """Class for tracking customers arriving in a donut shop."""
    __slots__ = ['queue']
    queue: List[Customer]
    
    def __init__(self) -> None:
        self.queue = []
    
    def arrive(self, name: str, vip: bool) -> None:
        """ Add a new costumer to the queue """
        costumer: Customer = Customer(name, vip)
        if len(self.queue) == 0 or not costumer.vip:
            self.queue.insert(0, costumer)
            return
        next_position: int = self._next_vip_index()
        if next_position < 0:
            self.queue.append(costumer)
            return
        self.queue.insert(next_position, costumer)
    
    def next_customer(self) -> Optional[str]:
        """ Returns the costumer in the last position of the list"""
        if len(self.queue) == 0:
            return None
        return self.queue.pop().name

    def _next_vip_index(self) -> int:
        """ Returns the index of the next vip costumer or -1 if not found"""
        for index, costumer in enumerate(self.queue):
            if costumer.vip:
                return index
        return -1

    def waiting(self) -> Optional[str]:
        """
            Returns a comma separated string with the names of the customers
            waiting in the order they will be served or None if there are
            no customers waiting.
        """
        if len(self.queue) == 0:
            return None
        queue: List[Customer] = self.queue.copy()
        queue.reverse()

        return ', '.join(map(lambda costumer: costumer.name, queue))
