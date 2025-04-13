"""
Name: simple_tokenizer.py
Description: Converts text into token IDs, splitting on whitespace and punctuation.
Author: Connor Kasarda
Date: 2025-04-12
"""

import re

class SimpleTokenizer:
    """
    A class to tokenize text into token IDs.
    """

    def tokenize(self, text: str) -> list[int]:
        """
        Processes the text and converts it into IDs.

        Args:
            text (str): The input text to be tokenized.

        Returns:
            list: A list of token IDs corresponding to the input text.
        """

        return re.findall(r'([a-zA-Z]+|[!?\'";:,.()]|--)', text)