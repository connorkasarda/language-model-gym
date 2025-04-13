"""
Name: simple_tokenizer.py
Description: A simple tokenizer that splits text into words and punctuation.
Author: Connor Kasarda
Date: 2025-04-12
"""

import re
from tokenization.tokenizer import Tokenizer

class SimpleTokenizer(Tokenizer):
    """
    A simple tokenizer that splits text into words and punctuation.
    """

    def __init__(self) -> None:
        """
        Initializes the SimpleTokenizer instance.
        """
        super().__init__()

    def tokenize(self, text: str) -> list[str]:
        """
        Tokenizes the input text into a list of tokens using a simple regex-based approach.

        Args:
            text (str): The input text to tokenize.

        Returns:
            list[str]: A list of tokens extracted from the input text.
        """
        # Use regex to split the text into words and punctuation
        tokens = re.findall(r'[a-zA-Z]+|[,.;:\'"!?()]|--', text)
        return tokens
    