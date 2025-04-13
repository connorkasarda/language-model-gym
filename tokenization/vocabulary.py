"""
Name: vocabulary.py
Description: Vocabulary class for managing token to id mappings and vice versa.
Author: Connor Kasarda
Date: 2025-04-12
"""

class Vocabulary:

    def __init__(self, tokens: list[str]=None, special_tokens: list[str]=None):
        """
        Initialize the Vocabulary with mappings between tokens and ids.

        Args:
            tokens (list[str]): List of tokens to include in the vocabulary.
            special_tokens (list[str]): List of special tokens to include in the vocabulary.
        """

        if tokens is None:
            tokens = []
        if special_tokens is None:
            special_tokens = []

        all_tokens = special_tokens + sorted(set(tokens) - set(special_tokens))
        self.token_2_id_map = {token : id for id, token in enumerate(sorted(set(all_tokens)))}
        self.id_2_token_map = {id : token for id, token in self.token_2_id_map.items()}