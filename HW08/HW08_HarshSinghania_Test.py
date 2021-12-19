'''

Author - Harsh Singhania
CWID - 20007289
SSW 810 - HW 08
Test suite file for HW08 - Date arithmetic operations, Field separated file reader, 
Scanning directories and file.

'''

import unittest
from typing import List, Tuple
from datetime import datetime
from HW08_HarshSinghania import date_arithmetic, file_reader, FileAnalyzer


class DateArithmeticTest(unittest.TestCase):
    """Test suite for date_arithmetic"""

    def test_date_arithmetic(self) -> None:
        """Tests the function date_arithmetic"""
        three_days_after_02272020: datetime
        three_days_after_02272019: datetime
        diff: int

        three_days_after_02272020, three_days_after_02272019, \
            diff = date_arithmetic()

        self.assertEqual(three_days_after_02272020, datetime(2020, 3, 1))
        self.assertEqual(three_days_after_02272019, datetime(2019, 3, 2))
        self.assertEqual(diff, 241)


class FileReaderTest(unittest.TestCase):
    """Test suite for file_reader"""

    def test_file_reader(self) -> None:
        """Tests the function file_reader"""
        file_path: str = "/Users/harshsinghania/Desktop/SSW 810/hw08/student_majors.txt"
        error_file_path: str = "/Users/harshsinghania/Desktop/SSW 810/hw08/tests/error.txt"
        dir_file_path: str = "/Users/harshsinghania/Desktop/SSW 810/hw08"
        invalid_file_path: str = "/Users/harshsinghania/Desktop/SSW 810/hw08/non_existent.txt"

        with self.assertRaises(FileNotFoundError):
            tuple(file_reader(invalid_file_path, 20))

        with self.assertRaises(IsADirectoryError):
            tuple(file_reader(dir_file_path, 20))

        with self.assertRaises(ValueError):
            list(file_reader(file_path, 2, "|", True))

        with self.assertRaises(ValueError):
            list(file_reader(error_file_path, 2, "|", True))

        response: List[Tuple[str]] = list(file_reader(file_path, 3, "|"))
        self.assertEqual(response, [
            ("CWID", "Name", "Major"),
            ("123", "Jin He", "Computer Science"),
            ("234", "Nanda Koka", "Software Engineering"),
            ("345", "Benji Cai", "Software Engineering")
        ])

        response = list(file_reader(file_path, 3, "|", True))
        self.assertEqual(response, [
            ("123", "Jin He", "Computer Science"),
            ("234", "Nanda Koka", "Software Engineering"),
            ("345", "Benji Cai", "Software Engineering")
        ])


class FileAnalyzerTest(unittest.TestCase):
    """Test suite for FileAnalyzer"""

    def test_file_analyzer(self) -> None:
        file_path: str = "/Users/harshsinghania/Desktop/SSW 810/hw08/student_majors.txt"
        dir_path: str = "/Users/harshsinghania/Desktop/SSW 810/hw08/tests"

        first_file = '0_defs_in_this_file.py'
        second_file = 'HW08_HarshSinghania.py'
        third_file = 'HW05_HarshSinghania.py'

        with self.assertRaises(FileNotFoundError):
            FileAnalyzer("/hw08/example")

        with self.assertRaises(ValueError):
            FileAnalyzer(file_path)

        file_analyzer: FileAnalyzer = FileAnalyzer(dir_path)
        self.assertEqual(len(file_analyzer.files_summary.keys()), 4)
        self.assertEqual(file_analyzer.files_summary[first_file], {
            "class": 0,
            "function": 0,
            "line": 3,
            "char": 57
        })
        self.assertEqual(file_analyzer.files_summary[second_file], {
            "class": 2,
            "function": 8,
            "line": 180,
            "char": 5903
        })
        self.assertEqual(file_analyzer.files_summary[third_file], {
            "class": 0,
            "function": 6,
            "line": 121,
            "char": 3519
        })
        file_analyzer.pretty_print()


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
