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

    def __init__(self, max_num_merges: int = 10000) -> None:
        """
        Initializes the BytePairEncoding instance.

        Args:
            max_num_merges (int): The maximum number of token-pair merges to perform. Default is 10000.
        """
        
        super().__init__()
        self.max_num_merges = max_num_merges

    def segment(self, text: str, max_num_merges: int = None) -> list[str]:
        """
        Tokenizes the input text into a list of tokens using byte pair encoding.
        Maximum number of token-pair merges can be specified.

        Args:
            text (str): The input text to tokenize.
            max_num_merges (int, optional): The maximum number of token-pair merges to perform. If None, uses the default value.

        Returns:
            list[str]: A list of tokens extracted from the input text.
        """

        tokenized_text = list(text)
        if max_num_merges is None:
            max_num_merges = self.max_num_merges
        for _ in max_num_merges:
            most_frequent_token_pair = self.find_most_frequent_token_pair(tokenized_text)
            if most_frequent_token_pair is None:
                break
            tokenized_text = self.add_new_token_pair(most_frequent_token_pair, tokenized_text)
        return tokenized_text
    
    def find_most_frequent_token_pair(self, tokenized_text: list[str]) -> tuple[str, str]:
        """
        Finds the most frequent pair of adjacent symbols in the tokenized text.

        Args:
            tokenized_text (list[str]): The tokenized text to search for the most frequent token pair.

        Returns:
            tuple[str, str]: The most frequent token pair found in the tokenized text.
        """

        token_pairs = {}
        for token_idx in range(len(tokenized_text) - 1):
            token_pair = (tokenized_text[token_idx], tokenized_text[token_idx + 1])
            token_pairs[token_pair] = token_pairs.get(token_pair, 0) + 1
        if not token_pairs:
            return None
        return max(token_pairs, key=token_pairs.get)
    
    def add_new_token_pair(self, token_pair: tuple[str, str], tokenized_text: list[str]) -> list[str]:
        """
        Adds a new token pair to the tokenized text by merging the most frequent token pair.

        Args:
            token_pair (tuple[str, str]): The token pair to merge.
            tokenized_text (list[str]): The tokenized text to update.

        Returns:
            list[str]: The updated tokenized text with the new token pair added.
        """

        new_token = ''.join(token_pair)
        updated_tokenized_text = []
        skip_token = False
        for token_idx in range(len(tokenized_text) - 1):
            if skip_token:
                skip_token = False
                continue
            if (tokenized_text[token_idx], tokenized_text[token_idx + 1]) == token_pair:
                updated_tokenized_text.append(new_token)
                skip_token = True
            else:
                updated_tokenized_text.append(tokenized_text[token_idx])
        if not skip_token:
            updated_tokenized_text.append(tokenized_text[-1])
        tokenized_text = updated_tokenized_text
        return tokenized_text