"""
Name: vocabulary.py
Description: Vocabulary class for tokenization
Author: Connor Kasarda
Date: 2025-04-13
"""

class Vocabulary:
    """
    A class to manage a vocabulary for tokenization.

    Methods:
        __init__: Initializes an empty Vocabulary.
        build: Builds the vocabulary from a given text.
        get_id: Returns the ID of a token.
        get_token: Returns the token corresponding to an ID.
        __len__: Returns the size of the vocabulary.
    """

    def __init__(
        self,
        max_size: int = 10000,
        UNKNOWN_TOKEN: str = '<UNK>',
        PADDING_TOKEN: str = '<PAD>',
        BEGIN_OF_SEQ_TOKEN: str = '<BOS>',
        END_OF_SEQ_TOKEN: str = '<EOS>'
    ) -> None:
        """
        Initializes an empty Vocabulary.

        Args:
            max_size (int): The maximum size of the vocabulary.
            UNKNOWN_TOKEN (str): The token representing unknown words.
            PADDING_TOKEN (str): The token representing padding.
            BEGIN_OF_SEQ_TOKEN (str): The token representing the beginning of a sequence.
            END_OF_SEQ_TOKEN (str): The token representing the end of a sequence.
        
        Attributes:
            max_size (int): The maximum size of the vocabulary.
            UNKNOWN_TOKEN (str): The token representing unknown words.
            PADDING_TOKEN (str): The token representing padding.
            BEGIN_OF_SEQ_TOKEN (str): The token representing the beginning of a sequence.
            END_OF_SEQ_TOKEN (str): The token representing the end of a sequence.
            UNKNOWN_ID (int): The ID for the unknown token.
            PADDING_ID (int): The ID for the padding token.
            BEGIN_OF_SEQ_ID (int): The ID for the beginning of sequence token.
            END_OF_SEQ_ID (int): The ID for the end of sequence token.
            token_2_id_map (dict): A mapping from tokens to their unique IDs.
            id_2_token_map (dict): A mapping from unique IDs to their corresponding tokens.
        """

        self.max_size = max_size
        self.UNKNOWN_TOKEN = UNKNOWN_TOKEN
        self.PADDING_TOKEN = PADDING_TOKEN
        self.BEGIN_OF_SEQ_TOKEN = BEGIN_OF_SEQ_TOKEN
        self.END_OF_SEQ_TOKEN = END_OF_SEQ_TOKEN
        self.UNKNOWN_ID = None
        self.PADDING_ID = None
        self.BEGIN_OF_SEQ_ID = None
        self.END_OF_SEQ_ID = None
        self.token_2_id_map = {}
        self.id_2_token_map = {}

    def build(self, tokens: list[str] = None) -> None:
        """
        Builds the vocabulary from a given text.

        Args:
            tokens (list[str]): The tokens to build the vocabulary from.
                If None, initializes an empty vocabulary.
        """

        if tokens is None:
            tokens = []

        special_tokens = [self.UNKNOWN_TOKEN, self.PADDING_TOKEN, self.BEGIN_OF_SEQ_TOKEN, self.END_OF_SEQ_TOKEN]
        unique_tokens = sorted(set(tokens) - set(special_tokens))
        limited_tokens = unique_tokens[:self.max_size - len(special_tokens)]
        all_tokens = special_tokens + limited_tokens

        self.token_2_id_map = {token: id for id, token in enumerate(all_tokens)}
        self.id_2_token_map = {id: token for token, id in self.token_2_id_map.items()}

        self.UNKNOWN_ID = self.token_2_id_map[self.UNKNOWN_TOKEN]
        self.PADDING_ID = self.token_2_id_map[self.PADDING_TOKEN]
        self.BEGIN_OF_SEQ_ID = self.token_2_id_map[self.BEGIN_OF_SEQ_TOKEN]
        self.END_OF_SEQ_ID = self.token_2_id_map[self.END_OF_SEQ_TOKEN]

    def get_id(self, token: str) -> int:
        """
        Returns the ID of a token.

        Args:
            token (str): The token to look up.

        Returns:
            int: The ID of the token, or the ID for the unknown token if not found.
        """

        return self.token_2_id_map.get(token, self.UNKNOWN_ID)
    
    def get_token(self, id: int) -> str:
        """
        Returns the token corresponding to an ID.

        Args:
            id (int): The ID to look up.

        Returns:
            str: The token corresponding to the ID, or the unknown token if not found.
        """

        return self.id_2_token_map.get(id, self.UNKNOWN_TOKEN)

    def __len__(self) -> int:
        """
        Returns the size of the vocabulary.
        """

        return len(self.token_2_id_map)
