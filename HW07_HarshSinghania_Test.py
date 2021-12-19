'''

Author - Harsh Singhania
CWID - 20007289
SSW 810 - HW07
Test suite file for HW07 - Anagrams, Covers Alphabets & Web Analyzer.

'''
import unittest
from typing import List, Tuple
from HW07_HarshSinghania import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer

class TestAnagramList(unittest.TestCase):
    """Test Cases for Part 1: Anagram"""
    def test_anagrams_list(self) -> None:    
        """Test cases for Anagrams List function."""
        self.assertEqual(anagrams_lst("cinema","iceman"),True)
        self.assertEqual(anagrams_lst("dormitory","dirtyroom"),True)
        self.assertEqual(anagrams_lst("dormitory","dirty"), False)
    
    def test_anagrams_dd(self) -> None:
        """Test cases for Anagrams using DefaultDict function"""
        self.assertEqual(anagrams_dd("hello", "olleh"), True)
        self.assertEqual(anagrams_dd("hello", "holle"), True)
        self.assertEqual(anagrams_dd("dusty", "study"), True)
        self.assertEqual(anagrams_dd("hello", "ollehh"), False)

    def test_anagrams_cntr(self) -> None:
        """Test cases for Anagrams using counter"""
        self.assertEqual(anagrams_cntr("hello", "olleh"), True)
        self.assertEqual(anagrams_cntr("dusty", "study"), True)
        self.assertEqual(anagrams_cntr("hello", "ollehh"), False)
        self.assertEqual(anagrams_cntr("hello", "ollehh"), False)

class CoversAlphabetTest(unittest.TestCase):
    """Test suite for covers alphabet"""
    def test_covers_alphabet(self) -> None:
        """Tests covers_alphabet function"""
        self.assertEqual(covers_alphabet("abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"), True)
        self.assertEqual(covers_alphabet("The quick brown fox jumps over the "
                                        "lazy dog"), True)
        self.assertEqual(covers_alphabet("We promptly judged antique ivory "
                                        "buckles for the next prize"), True)
        self.assertEqual(covers_alphabet("abcdefghijklmnopqrstuvwxy"), False)
        self.assertEqual(covers_alphabet("bcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(covers_alphabet(""), False)
        self.assertEqual(covers_alphabet("xyz"), False)
        self.assertEqual(covers_alphabet("The quick, brown, fox; jumps over "
                                        "the lazy dog!"), True)

class WebAnalyzerTest(unittest.TestCase):
    """Test suite for Web analyzer"""
    def test_web_analyzer(self) -> None:
        """Tests web_analyzer function"""
        weblogs: List[Tuple[str, str]] = [
            ("Nanda", "google.com"),
            ("Maha", "google.com"),
            ("Fei", "python.org"),
            ("Maha", "google.com"),
            ("Fei", "python.org"),
            ("Nanda", "python.org"),
            ("Fei", "dzone.com"),
            ("Nanda", "google.com"),
            ("Maha", "google.com"),
        ]
        summary: List[Tuple[str, List[str]]] = [
            ("dzone.com", ["Fei"]),
            ("google.com", ["Maha", "Nanda"]),
            ("python.org", ["Fei", "Nanda"]),
        ]
        self.assertEqual(web_analyzer(weblogs), summary)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
