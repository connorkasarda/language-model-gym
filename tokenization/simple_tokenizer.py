"""
Name: simple_tokenizer.py
Description: Converts text into token IDs, splitting on whitespace and punctuation.
Author: Connor Kasarda
Date: 2025-04-12
"""

import re
import string

class SimpleTokenizer:
    """
    A class to tokenize text into token IDs.

    Attributes:
        token_2_id_map (dict): A dictionary mapping tokens to IDs.
        id_2_token_map (dict): A dictionary mapping IDs to tokens.
    """

    def __init__(self, vocab: dict[str, int]):
        self.token_2_id_map = vocab
        self.id_2_token_map = { id : token for token, id in vocab.items() }

    def encode(self, text: str) -> list[int]:
        """
        Processes the text and converts it into IDs.

        Args:
            text (str): The input text to be tokenized.

        Returns:
            list: A list of token IDs corresponding to the input text.
        """

        tokens = re.findall(r'([a-zA-Z]+|[!?\'";:,.()]|--)', text)
        return [self.token_2_id_map[token] for token in tokens]

    def decode(self, ids: list[int]) -> str:
        """
        Processes the token IDs and converts them into text.

        Args:
            token_ids (list): The list of token IDs to be converted into text.

        Returns:
            str: The decoded text corresponding to the input token IDs.
        """

        text = []
        for iter, id in enumerate(ids):
            token = self.id_2_token_map[id]
            if iter > 0 and token not in string.punctuation:
                text.append(' ')
            text.append(token)
        return ''.join(text)