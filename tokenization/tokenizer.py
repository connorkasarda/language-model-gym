"""
Name: tokenizer.py
Description: This module contains the base Tokenizer class.
Author: Connor Kasarda
Date: 2025-04-13
"""

import string
from tokenization.vocabulary import Vocabulary

class Tokenizer:
    """
    Base class for tokenizers.

    Attributes:
        vocab (Vocabulary): An instance of the Vocabulary class used for encoding and decoding tokens.

    Methods:
        __init__() -> None: Initializes the Tokenizer instance.
        learn(text: str) -> None: Trains the tokenizer on the provided text.
        segment(text: str) -> list[str]: Tokenizes the input text into a list of tokens.
        encode(text: str) -> list[int]: Encodes the input text into a list of token IDs.
        decode(token_ids: list[int]) -> str: Decodes a list of token IDs back into the original text.
    """

    def __init__(self) -> None:
        """
        Initializes the Tokenizer instance.
        """
        
        self.vocab = Vocabulary()

    def learn(self, text: str) -> None:
        """
        Trains the tokenizer on the provided text. Builds a vocabulary from the text.

        Args:
            text (str): The input text to train on.
        """

        tokenized_text = self.segment(text)
        self.vocab.build(tokenized_text)

    def segment(self, text: str) -> list[str]:
        """
        Tokenizes the input text into a list of tokens.

        Args:
            text (str): The input text to tokenize.

        Returns:
            list[str]: A list of tokens extracted from the input text.
        """

        raise NotImplementedError("Subclasses must implement this method.")
    
    def encode(self, text: str) -> list[int]:
        """
        Encodes the input text into a list of token IDs using the vocabulary.

        Args:
            text (str): The input text to encode.

        Returns:
            list[int]: A list of token IDs corresponding to the input text.
        """

        token_ids = []
        left_text_pointer = 0
        while left_text_pointer < len(text):
            token_found = False
            for right_text_pointer in range(len(text), left_text_pointer, -1):
                token = text[left_text_pointer:right_text_pointer]
                token_id = self.vocab.get_id(token)
                if token_id != self.vocab.UNKNOWN_ID:
                    token_ids.append(token_id)
                    left_text_pointer = right_text_pointer
                    token_found = True
                    break
            if not token_found:
                token_ids.append(self.vocab.UNKNOWN_ID)
                left_text_pointer += 1
        return token_ids
    
    def decode(self, token_ids: list[int]) -> str:
        """
        Decodes a list of token IDs back into the original text using the vocabulary.

        Args:
            token_ids (list[int]): A list of token IDs to decode.

        Returns:
            str: The decoded text.
        """

        tokenzied_text = []
        for iter, token_id in enumerate(token_ids):
            token = self.vocab.get_token(token_id)
            tokenzied_text.append(token)
        return ''.join(tokenzied_text)
    
    def __len__(self) -> int:
        """
        Returns the size of the vocabulary.

        Returns:
            int: The size of the vocabulary.
        """

        return len(self.vocab)
