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
        train(text: str) -> None: Trains the tokenizer on the provided text.
        tokenize(text: str) -> list[str]: Tokenizes the input text into a list of tokens.
        encode(text: str) -> list[int]: Encodes the input text into a list of token IDs.
        decode(token_ids: list[int]) -> str: Decodes a list of token IDs back into the original text.
    """

    def __init__(self) -> None:
        """
        Initializes the Tokenizer instance.
        """
        
        self.vocab = Vocabulary()

    def train(self, text: str) -> None:
        """
        Trains the tokenizer on the provided text. Builds a vocabulary from the text.

        Args:
            text (str): The input text to train on.
        """

        tokens = self.tokenize(text)
        self.vocab.build(tokens)

    def tokenize(self, text: str) -> list[str]:
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
        Encodes the input text into a list of token IDs.

        Args:
            text (str): The input text to encode.

        Returns:
            list[int]: A list of token IDs corresponding to the input text.
        """

        tokens = self.tokenize(text)
        return [self.vocab.get_id(token) for token in tokens]
    
    def decode(self, token_ids: list[int]) -> str:
        """
        Decodes a list of token IDs back into the original text.

        Args:
            token_ids (list[int]): A list of token IDs to decode.

        Returns:
            str: The decoded text.
        """

        tokens = []
        for iter, token_id in enumerate(token_ids):
            token = self.vocab.get_token(token_id)
            if iter != 0 and token not in string.punctuation:
                tokens.append(' ')
            tokens.append(token)
        return ''.join(tokens)
    
    def __len__(self) -> int:
        """
        Returns the size of the vocabulary.

        Returns:
            int: The size of the vocabulary.
        """

        return len(self.vocab)
