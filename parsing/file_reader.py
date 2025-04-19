"""
Name: file_reader.py
Description: This module contains the FileReader class for reading files and returning their contents.
Author: Connor Kasarda
Date: 2025-04-16
"""

from typing import Iterator

class FileReader:
    """
    Interface for file readers that return file contents as a string object.

    Attributes:
        None

    Methods:
        __init__() -> None:
            Initializes the FileReader instance.
        read_all(path: str, encoding: str = 'utf-8') -> str:
            Returns the contents of the file as a string.
        read_lines(path: str, encoding: str = 'utf-8') -> Iterator[str]:
            Provides an iterator that yields lines from the file one by one.
        read_chunks(path: str, chunk_size: int = 1024, encoding: str = 'utf-8') -> Iterator[str]:
            Provides an iterator that yields chunks of the file one by one.
    """

    def __init__(self) -> None:
        """
        Initializes the FileReader instance.
        """

        pass

    def read_all(self, path: str, encoding: str = 'utf-8') -> str:
        """
        Returns the contents of the file as a string.

        Args:
            path (str): The path to the file.
            encoding (str): The encoding of the file. Defaults to 'utf-8'.

        Returns:
            str: The contents of the file as a string.
        """

        raise NotImplementedError('Subclasses must implement this method.')
    
    def read_lines(self, path: str, encoding: str = 'utf-8') -> Iterator[str]:
        """
        Provides an iterator that yields lines from the file one by one.

        Args:
            path (str): The path to the file.
            encoding (str): The encoding of the file. Defaults to 'utf-8'.

        Returns:
            Iterator[str]: An iterator that yields lines from the file.
        """

        raise NotImplementedError('Subclasses must implement this method.')

    def read_chunks(self, path: str, chunk_size: int = 1024, encoding: str = 'utf-8') -> Iterator[str]:
        """
        Provides an iterator that yields chunks of the file one by one.

        Args:
            path (str): The path to the file.
            chunk_size (int): The size of each chunk in bytes. Defaults to 1024.
            encoding (str): The encoding of the file. Defaults to 'utf-8'.

        Returns:
            Iterator[str]: An iterator that yields chunks of the file.
        """

        raise NotImplementedError('Subclasses must implement this method.')