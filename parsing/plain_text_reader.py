"""
Name: txt_file_reader.py
Description: This module contains the TxtFileReader class for reading in plain text files and returning their contents.
Author: Connor Kasarda
Date: 2025-04-17
"""

from typing import Iterator
from parsing.file_reader import FileReader

class PlainTextReader(FileReader):
    """
    Class for reading in plain text files and returning their contents.
    Inherits from the FileReader class.

    Attributes:
        None

    Methods:
        __init__() -> None:
            Initializes the TxtFileReader instance.
        read_all(path: str, encoding: str = 'utf-8') -> str:
            Returns the contents of the text file as a string.
        read_lines(path: str, encoding: str = 'utf-8') -> Iterator[str]:
            Provides an iterator that yields lines from the text file one by one.
        read_chunks(path: str, chunk_size: int = 1024, encoding: str = 'utf-8') -> Iterator[str]:
            Provides an iterator that yields chunks of the text file one by one.
    """

    def __init__(self) -> None:
        """
        Initializes the TxtFileReader instance.
        """
        
        super().__init__()

    def read_all(self, path: str, encoding: str = 'utf-8') -> str:
        """
        Returns the contents of the text file as a string.

        Args:
            path (str): The path to the text file.
            encoding (str): The encoding of the text file. Defaults to 'utf-8'.

        Returns:
            str: The contents of the text file as a string.
        """

        with open(path, 'r', encoding=encoding) as file:
            return file.read()
        
    def read_lines(self, path: str, encoding: str = 'utf-8') -> Iterator[str]:
        """
        Provides an iterator that yields lines from the text file one by one.

        Args:
            path (str): The path to the text file.
            encoding (str): The encoding of the text file. Defaults to 'utf-8'.

        Returns:
            Iterator[str]: An iterator that yields lines from the text file.
        """

        with open(path, 'r', encoding=encoding) as file:
            for line in file:
                yield line

    def read_chunks(self, path, chunk_size = 1024, encoding = 'utf-8') -> Iterator[str]:
        """
        Provides an iterator that yields chunks of the text file one by one.

        Args:
            path (str): The path to the text file.
            chunk_size (int): The size of each chunk in bytes. Defaults to 1024.
            encoding (str): The encoding of the text file. Defaults to 'utf-8'.

        Returns:
            Iterator[str]: An iterator that yields chunks of the text file.
        """

        with open(path, 'r', encoding=encoding) as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk