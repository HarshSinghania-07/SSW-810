'''

NAME: HARSH SINGHANIA 
SSW 810 - HW05_Test
CWID - 20007289

Test Suite file for testing all the test cases in our main code.

'''

from typing import List, Iterator
from pathlib import Path
import unittest
from HW05_HarshSinghania import find_second, reverse, get_lines, substring

class TestString(unittest.TestCase):
    """Class TestString is used to test all the functions"""

    def test_reverse(self):
        """Test cases for reversing the string function."""

        self.assertEqual(reverse("Hello world"), "dlrow olleH")
        self.assertEqual(reverse(" "), " ")
        self.assertEqual(reverse("good day to you!"), "!uoy ot yad doog")
    
    def test_substring(self):
        """Test cases for substring function."""

        self.assertEqual(substring("he", "hello"), 0)
        self.assertEqual(substring("ell", "hello"), 1)
        self.assertEqual(substring("xxx", "hello"), -1)
        self.assertEqual(substring("o", "hello"), 4)

    def test_find_second(self):
        """Test cases for finding second occurence function."""

        self.assertEqual(find_second('iss', 'Mississippi'), 4)
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertEqual(find_second("l", "hello"), 3)
        self.assertEqual(find_second("ba", "abbabba"), 5)
        self.assertEqual(find_second('abc', ' '), -1)
        
class GetLinesTest(unittest.TestCase):
    def test_get_lines(self):
        """contains the test cases for get_lines()"""
        test_file_path = '/Users/harshsinghania/Desktop/STEVENS UPDATED/SSW 810/HW05_Test.txt'
        expect: List[str] = [
            '<line0>',
            '<line1>',
            '<line2>',
            '<line3.1 line3.2 line3.3>',
            '<line4.1 line4.2>',
            '<line5>',
            '<line6>'
        ]
        result: List[str] = list(get_lines(test_file_path))
        self.assertEqual(result, expect)

class DonutQueueTest(unittest.TestCase):
    def test_queue(self):
         dq = DonutQueue()
         self.assertIsNone(dq.next_customer())
         dq.arrive("Sujit", False)
         dq.arrive("Fei", False)
         dq.arrive("Prof JR", True)
         self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
         dq.arrive("Nanda", True)
         self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
         self.assertEqual(dq.next_customer(), "Prof JR")
         self.assertEqual(dq.next_customer(), "Nanda")
         self.assertEqual(dq.next_customer(), "Sujit")
         self.assertEqual(dq.waiting(), "Fei")
         self.assertEqual(dq.next_customer(), "Fei")
         self.assertIsNone(dq.next_customer())
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)