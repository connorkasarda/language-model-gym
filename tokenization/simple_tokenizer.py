"""
Name: simple_tokenizer.py
Description: A simple tokenizer that splits text into words and punctuation including spaces in the tokens.
Author: Connor Kasarda
Date: 2025-04-12

Warning:
    Use at your own risk. The author is not responsible for any damages or losses incurred from using this code.
"""

import re
from tokenization.tokenizer import Tokenizer

class SimpleTokenizer(Tokenizer):
    """
    A simple tokenizer that splits text into words and punctuation.

    Methods:
        __init__(): Initializes the SimpleTokenizer instance.
        segment(text: str) -> list[str]: Tokenizes the input text into a list of tokens.
    """

    def __init__(self) -> None:
        """
        Initializes the SimpleTokenizer instance.
        """
        
        super().__init__()

    def segment(self, text: str) -> list[str]:
        """
        Tokenizes the input text into a list of tokens with whitespace included.

        Args:
            text (str): The input text to tokenize.

        Returns:
            list[str]: A list of tokens extracted from the input text.
        """
        
        tokens = re.findall(r' ?[\w]+|[^\w\s]', text)
        return tokens
