'''

Author - Harsh Singhania
CWID - 20007289
SSW 810 - HW 08 Python parameters, modules, files, and the web
Part 1 - Date Arithmetic Operations
Part 2 - Field separated file reader
Part 3 - Scanning directories and files

'''

import os
from pathlib import Path
from datetime import datetime, timedelta, date
from typing import Dict, Tuple, Iterator, List
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ Tuple that returns two datetime and one int.
        1. An instance of  class datetime representing the date three days
        after Feb 27, 2020.
        2. An instance of  class datetime representing the date three days
        after Feb 27, 2019.
        3. An int representing the number of days between
        Feb 1, 2019 and Sept 30, 2019
    ."""

    first_input_date: datetime = datetime(2020, 2, 27)
    second_input_date: datetime = datetime(2019, 2, 27)

    days_delta: timedelta = timedelta(days=3)
    days_passed: int = (date(2019, 9, 30) - date(2019, 2, 1)).days

    return first_input_date + days_delta, \
           second_input_date + days_delta, \
           days_passed


def file_reader(path: str, fields: int, sep: str = ",",
                header: bool = False) -> Iterator[Tuple[str]]:
    """Return a generator using a file and split using separators"""

    if not os.path.exists(path):
        raise FileNotFoundError(f'the path {path} do not exist')

    file_path = Path(path)
    if not file_path.is_file():
        raise IsADirectoryError(f'the path {path} is a directory')

    line_counter: int = 0
    try:
        with open(path, "r") as file:
            for line in file.readlines():
                line = line.strip('\n')
                line_counter += 1

                terms: List[str] = line.split(sep) if len(line) > 0 else []

                if len(terms) != fields:
                    raise ValueError(f"expect {fields} but {len(terms)} were "
                                     f"found")

                if header and line_counter == 1:
                    continue

                yield tuple(terms)
            else:
                file.close()
    except IOError as e:
        print(f'Error working with the file {file_path} \n{str(e)}')
    except ValueError as e:
        raise ValueError(
            f"Error in file '{file_path}' line {line_counter} \n{str(e)}")


class FileData:
    __slots__ = ['name', 'lines', 'characters', 'functions', 'classes']
    """ Represents a object summary from the file."""

    def __init__(self, name: str, lines: int = 0, characters: int = 0,
                 functions: int = 0, classes: int = 0) -> None:
        
        self.name = name
        self.lines = lines
        self.characters = characters
        self.functions = functions
        self.classes = classes


def _is_a_python_file(path: str) -> bool:
    """Check if the path is a python file"""
    file_path: Path = Path(path)
    if not os.path.exists(path) or not file_path.is_file():
        return False
    extension = os.path.splitext(path)[1][1:]
    return extension == 'py'


def _analyze_file(path: str) -> FileData:
    """Get the information data from a python file path"""
    if not os.path.exists(path):
        raise FileNotFoundError(f'the path {path} do not exist')

    file_path = Path(path)
    if not file_path.is_file():
        raise IsADirectoryError(f'the path {path} is a directory')

    data: FileData = FileData(name=path)
    with open(path, "r") as file:
        for line in file.readlines():
            data.lines += 1
            if len(line) == 0:
                continue
            data.characters += len(list(line))
            if line.strip().startswith('def '):
                data.functions += 1
                continue
            if line.strip().startswith('class '):
                data.classes += 1
                continue
        else:
            file.close()
    return data


class FileAnalyzer:
    """ Given a directory name, searches that directory for Python files and analyze results
        (i.e. files ending with .py)."""

    def __init__(self, directory: str = os.curdir) -> None:
        """ Constructor for the analyzer"""
        if not os.path.exists(directory):
            raise FileNotFoundError(f'path {directory} do not exist')

        file_path: Path = Path(directory)
        if not file_path.is_dir():
            raise ValueError(f'path {directory} is not a directory')

        self.directory: str = directory                                     #optional
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """ Analyze a directory to get the files data"""
        files: List[str] = [os.path.abspath(os.path.join(self.directory, f))
                            for f in os.listdir(self.directory)]
        files_data: List[FileData] = [_analyze_file(file)
                                      for file in files
                                      if _is_a_python_file(file)]
        self.files_summary = {
            os.path.basename(data.name): {
                "class": data.classes,
                "function": data.functions,
                "line": data.lines,
                "char": data.characters
            } for data in files_data
        }

    def pretty_print(self) -> None:
        """Display the summary as a table"""
        table = PrettyTable()
        table.field_names = [
            "File Name",
            "Classes",
            "Functions",
            "Lines",
            "Characters"
        ]

        for file_name, data in self.files_summary.items():
            table.add_row([
                file_name,
                data['class'],
                data['function'],
                data['line'],
                data['char'],
            ])

        print(table)
