"""
name: test_plain_text_reader.py
Description: Unit tests for the PlainTextReader class.
Author: Connor Kasarda
Date: 2025-04-18

Warning:
    Use at your own risk. The author is not responsible for any damages or losses incurred from using this code.
"""

import unittest
from pathlib import Path
import textwrap
from parsing.plain_text_reader import PlainTextReader

class TestPlainTestReader(unittest.TestCase):
    """
    Test case for the PlainTextReader class.

    Attributes:
        reader (PlainTextReader): An instance of the PlainTextReader class.

    Methods:
        setUp() -> None:
            Set up a PlainTextReader instance for testing.
        test_read_all() -> None:
            Test reading all contents from a plain text file.
        test_read_lines() -> None:
            Test reading lines from a plain text file.
        test_read_chunks() -> None:
            Test reading chunks from a plain text file.
    """

    def setUp(self) -> None:
        """
        Set up a PlainTextReader instance for testing.

        Attributes:
            reader (PlainTextReader): An instance of the PlainTextReader class.
        """

        self.corpus_test_file = Path(__file__).parent.parent / 'corpus' / 'test.txt'
        if not self.corpus_test_file.exists():
            # Fail the test setup if the test file does not exist
            self.fail(f'Test file {self.corpus_test_file} does not exist.')
        self.reader = PlainTextReader()

    def test_read_all(self) -> None:
        """
        Test reading all contents from a plain text file.
        """
        
        expected_content = textwrap.dedent("""\
            This is just a test! I repeat; this is just a test.
            To be or not to be, that is the question.
            What is the answer to life, the universe, and everything?
            It's 42.
            The cake is a lie -- the biggest lie of all time.
            Where does the Earth end and Heaven begin?
            The answer is in the stars.
            """)
        actual_content = self.reader.read_all(self.corpus_test_file)
        self.assertEqual(expected_content, actual_content)

    def test_read_lines(self) -> None:
        """
        Test reading lines from a plain text file.
        """
        
        expected_lines = [
            "This is just a test! I repeat; this is just a test.\n",
            "To be or not to be, that is the question.\n",
            "What is the answer to life, the universe, and everything?\n",
            "It's 42.\n",
            "The cake is a lie -- the biggest lie of all time.\n",
            "Where does the Earth end and Heaven begin?\n",
            "The answer is in the stars.\n"
        ]
        actual_lines = list(self.reader.read_lines(self.corpus_test_file))
        self.assertEqual(expected_lines, actual_lines)

    def test_read_chunks(self) -> None:
        """
        Test reading chunks from a plain text file.
        """
        
        expected_chunks = [
            "This is just a test! I repeat; this is just a test",
            ".\nTo be or not to be, that is the question.\nWhat i",
            "s the answer to life, the universe, and everything",
            "?\nIt's 42.\nThe cake is a lie -- the biggest lie of",
            " all time.\nWhere does the Earth end and Heaven beg",
            "in?\nThe answer is in the stars.\n",
        ]
        actual_chunks = list(self.reader.read_chunks(self.corpus_test_file, chunk_size=50))
        self.assertEqual(expected_chunks, actual_chunks)