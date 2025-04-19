"""
Name: byte_pair_encoding.py
Description: Bottom-up tokenization using byte pair encoding (BPE) algorithm.
Author: Connor Kasarda
Date: 2025-04-18
"""

from tokenization.tokenizer import Tokenizer

class BytePairEncoding(Tokenizer):
    """
    Bottom-up tokenization using byte pair encoding (BPE) algorithm.

    Attributes:
        vocab (Vocabulary): An instance of the Vocabulary class used for encoding and decoding tokens.

    Methods:
        __init__(): Initializes the BytePairEncoding instance.
        segment(text: str) -> list[str]: Tokenizes the input text into a list of tokens using byte pair encoding.
    """

    def __init__(self) -> None:
        """
        Initializes the BytePairEncoding instance.
        """
        
        super().__init__()

    def segment(self, text: str) -> list[str]:
        """
        Tokenizes the input text into a list of tokens using byte pair encoding.

        Args:
            text (str): The input text to tokenize.

        Returns:
            list[str]: A list of tokens extracted from the input text.
        """

        pass