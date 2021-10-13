'''

Author - Harsh Singhania
CWID - 20007289
SSW 810 - HW 06 Test 
Test File for all the 6 parts mentioned in the main code file.

'''

from HW06_HarshSinghania import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, Customer, DonutQueue
import unittest
from typing import List, Iterator

class TestListCopy(unittest.TestCase):
    """Class for testing all test cases of List Copy Arguements."""
    def test_list_copy(self):
        """Test cases for List Copy Functions."""
        self.assertEqual(list_copy(['1']), ['1'])
        self.assertEqual(list_copy(['1','2']), ['1','2'])
        self.assertEqual(list_copy(['1','2','3']), ['1','2','3'])

    def test_type_errorr(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, list_copy, 0)
        self.assertRaises(TypeError, list_copy, "a")
        self.assertRaises(TypeError, list_copy, 11.1)

class TestListIntersect(unittest.TestCase):
    """Class for tesing all test cases of List Copy Arguements."""
    def test_list_intersect(self):
        """Test cases for List Intersect function."""
        self.assertEqual(list_intersect([1, 2, 3], [1, 4, 5]), [1])
        self.assertEqual(list_intersect([1, 2, 3], [1, 2, 4]), [1, 2])
        self.assertEqual(list_intersect([], []), [])

    def test_type_error(self) -> None:
        """Tests that only list are passed as Arguments"""
        self.assertRaises(TypeError, list_intersect, 0)
        self.assertRaises(TypeError, list_intersect, "a")
        self.assertRaises(TypeError, list_intersect, 11.1)
        self.assertRaises(TypeError, list_intersect, [])

class TestListDifference(unittest.TestCase):
    """Class for testing all test cases of List Difference Arguements."""
    def test_list_difference(self) -> None:
        """Test cases for List Difference function."""
        self.assertEqual(list_difference([1, 2, 3], [1, 2, 4]),[3])
        self.assertEqual(list_difference([1, 2, 3], [4, 5, 6]),[1, 2, 3])

    def test_type_error(self) -> None:
        """Tests that only list are passed as arguments"""
        self.assertRaises(TypeError, list_difference, 0)
        self.assertRaises(TypeError, list_difference, "a")
        self.assertRaises(TypeError, list_difference, 11.1)
        self.assertRaises(TypeError, list_difference, [])

class TestRemoveVowels(unittest.TestCase):
    """Class for testing all test cases of Remove Vowels Function"""
    def test_remove_vowels(self) -> None:
        """Test cases for Remove Vowels"""
        self.assertEqual(remove_vowels("Amy is my fav daughter"),"my fav daughter")
        self.assertEqual(remove_vowels("Amy is my only daughter"),"my daughter")
        self.assertEqual(remove_vowels("Jan is my best friend"),"Jan my best friend")

    def test_type_error(self) -> None:
        """Tests that only string is passed as an arguement."""
        self.assertRaises(TypeError, remove_vowels, 0)
        self.assertRaises(TypeError, remove_vowels, 11.1)
        self.assertRaises(TypeError, remove_vowels, [])

class TestPassword(unittest.TestCase):
    """Class for testing password checker function."""
    def test_check_pwd(self) -> None:
        self.assertEqual(check_pwd("123HarshS"), True)
        self.assertEqual(check_pwd("1HarshS"), True)
        self.assertEqual(check_pwd("Har"), False)
        self.assertEqual(check_pwd("xyz"), False)

class DonutQueueTest(unittest.TestCase):
    """Class for testing all tests cases in Donut Queue """
    def test_type_error(self) -> None:
        """Tests that only string and boolean are pass as arguments"""
        self.assertRaises(TypeError, Customer, 0)
        self.assertRaises(ValueError, Customer, "")
        self.assertRaises(TypeError, Customer, "Marcus", 9)
        self.assertRaises(TypeError, Customer, "James", "Bond")
    
    def test_queue(self):
        """Test cases for Donut Queue"""
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