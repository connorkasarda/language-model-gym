"""
Name: word_piece.py
Description: WordPiece tokenizer implementation.
Author: Connor Kasarda
Date: 2025-04-25

Warning:
    Use at your own risk. The author is not responsible for any damages or losses incurred from using this code.
"""

import regex as re
from tokenization.tokenizer import Tokenizer

class WordPiece(Tokenizer):
    """
    WordPiece tokenizer implementation.

    Attributes:
        vocab (Vocabulary): An instance of the Vocabulary class used for encoding and decoding tokens.

    Methods:
        __init__(): Initializes the WordPiece instance.
        segment(text: str, max_num_merges: int = None) -> list[str]: Tokenizes the input text into a list of tokens using WordPiece.
        encode(text: str) -> list[int]: Encodes the input text into a list of token IDs.
        decode(token_ids: list[int]) -> str: Decodes a list of token IDs back into the original text.
    """

    def __init__(self, max_num_merges: int = 10000) -> None:
        """
        Initializes the WordPiece instance.

        Args:
            max_num_merges (int): The maximum number of token-pair merges to perform. Default is 10000.
        """

        super().__init__()
        self.max_num_merges = max_num_merges

    def segment(self, text: str, max_num_merges: int = None) -> list[str]:
        """
        Tokenizes the input text into a list of tokens using the WordPiece algorithm.

        Args:
            text (str): The input text to tokenize.

        Returns:
            list[str]: A list of tokens extracted from the input text.
        """

        # If max_num_merges is not provided, use the default value
        if max_num_merges is None:
            max_num_merges = self.max_num_merges

        # Initialize with pre-tokenized text and frequency map
        words_puncs_spaces = re.findall(r'[\w]+|[^\w\s]+|\s', text)
        tokenized_text = list(text)
        token_2_freq_map = {}

        # Collect the frequencies of all tokens in the pre-tokenized text
        for token in tokenized_text:
            if token not in token_2_freq_map:
                token_2_freq_map[token] = 1
            else:
                token_2_freq_map[token] += 1

        # Perform the WordPiece algorithm to merge token pairs
        for _ in range(max_num_merges):
            token_pair = self.find_highest_scoring_token_pair(tokenized_text, token_2_freq_map)
            if token_pair is None:
                break
            tokenized_text = self.add_new_token_pair(token_pair, token_2_freq_map, tokenized_text)
        
        # Produce word pieces that would build up to the tokenized text
        return self.split_into_word_pieces(words_puncs_spaces, token_2_freq_map)

    def encode(self, text: str) -> list[int]:
        """
        Override of Tokenizer encode method to account for WordPiece prefix notation (i.e., ##).

        Args:
            text (str): The input text to encode.

        Returns:
            list[int]: A list of token IDs corresponding to the input text.
        """

        pass

    def decode(self, token_ids: list[int]) -> str:
        """
        Override of Tokenizer decode method to account for WordPiece prefix notation (i.e., ##).

        Args:
            token_ids (list[int]): A list of token IDs to decode.

        Returns:
            str: The decoded text.
        """

        pass
        
    def find_highest_scoring_token_pair(
            self,
            tokenized_text: list[str],
            token_2_freq_map: dict[str, int]) -> tuple[str, str]:
        """
        Finds the highest scoring token pair in the tokenized text.
        Score Function: (merge score) = (freq. of pair) / ((freq. of first token) * (freq. of second token))

        Args:
            tokenized_text (list[str]): The tokenized text to search for the highest scoring token pair.
            token_2_freq_map (dict[str, int]): A dictionary mapping tokens to their frequencies.

        Returns:
            tuple[str, str]: The highest scoring token pair found in the tokenized text.
        """

        # Create a dictionary to store the frequency of all occurring token pairs
        token_pair_2_freq_map = {}

        # Collect the frequency of all occuring token pairs in the tokenized text
        for token_idx in range(len(tokenized_text) - 1):
            token_pair = (tokenized_text[token_idx], tokenized_text[token_idx + 1])
            if token_pair not in token_pair_2_freq_map:
                token_pair_2_freq_map[token_pair] = 1
            else:
                token_pair_2_freq_map[token_pair] += 1

        # Calculate the score for each token pair and return the token pair with the highest score
        return (
            max(
                token_pair_2_freq_map,
                key=lambda pair: (
                    token_pair_2_freq_map[pair]
                    / (token_2_freq_map[pair[0]] * token_2_freq_map[pair[1]])
                ),
            )
            if token_pair_2_freq_map
            else None
        )
        
    def add_new_token_pair(
            self,
            token_pair: tuple[str, str],
            token_2_freq_map: dict[str, int],
            tokenized_text: list[str]) -> list[str]:
        """
        Adds a new token pair to the tokenized text by merging the highest scoring token pair.

        Args:
            token_pair (tuple[str, str]): The token pair to merge.
            token_2_freq_map (dict[str, int]): A dictionary mapping tokens to their frequencies.
            tokenized_text (list[str]): The tokenized text to update.

        Returns:
            list[str]: The updated tokenized text with the new token pair added.
        """

        # Create a new merged token from the token pair and initialize the updated tokenized text and skip token flag
        new_token = ''.join(token_pair)
        updated_tokenized_text = []
        skip_token = False

        # Iterate through the tokenized text
        for token_idx in range(len(tokenized_text) - 1):

            # We want to skip the token pair we just merged
            if skip_token:
                skip_token = False
                continue

            # Check if we found occurance of the token pair in the tokenized text
            if (
                tokenized_text[token_idx] == token_pair[0]
                and tokenized_text[token_idx + 1] == token_pair[1]
            ):
                
                # Add the new token to the updated tokenized text
                updated_tokenized_text.append(new_token)

                # Update the token frequency map where occurrences of token pair are
                token_2_freq_map[new_token] = token_2_freq_map.get(new_token, 0) + 1
                token_2_freq_map[token_pair[0]] -= 1
                token_2_freq_map[token_pair[1]] -= 1
                if token_2_freq_map[token_pair[0]] == 0:
                    del token_2_freq_map[token_pair[0]]
                if token_2_freq_map[token_pair[1]] == 0:
                    del token_2_freq_map[token_pair[1]]

                # Set the skip token flag to True to skip the next token in the tokenized text
                skip_token = True

            # Add the current token to the updated tokenized text if it is not part of the token pair
            else:
                updated_tokenized_text.append(tokenized_text[token_idx])

        # Add the last token in the tokenized text if it is not part of the token pair
        if not skip_token and tokenized_text:
            updated_tokenized_text.append(tokenized_text[-1])

        # Return the updated tokenized text
        return updated_tokenized_text

    def split_into_word_pieces(
            self,
            words_puncs_spaces: list[str],
            token_2_freq_map: dict[str, int]) -> list[str]:
        """
        Adds the WordPiece prefix notation (i.e., ##) to the tokenized text.

        Args:
            words_puncs_spaces (list[str]): The tokenized text to update.
            token_2_freq_map (dict[str, int]): A dictionary mapping tokens to their frequencies.

        Returns:
            list[str]: The updated tokenized text with the WordPiece prefix notation added.
        """

        # Create a new list to store the updated tokenized text with prefixes
        word_pieces = []

        # Add list of subwords w/o prefixes (i.e. "##") to build the words from the original text
        for token in words_puncs_spaces:
        
            # If the token is already a known token, just add it as is
            if token in token_2_freq_map:
                word_pieces.append(token)
                continue

            # Find word pieces that build up our token
            token_word_pieces = []
            while len(token) > 0:
                for pointer in range(len(token), 0, -1):
                    left_side = token[:pointer]
                    if left_side in token_2_freq_map:
                        token_word_pieces.append(left_side)
                        token = token[pointer:]
                        break
                else:
                    token_word_pieces.append(self.vocab.UNKNOWN_TOKEN)
                    break

            # Add "##" prefixes to word pieces where needed
            for piece_idx, piece in enumerate(token_word_pieces):
                if piece_idx == 0:
                    word_pieces.append(piece)
                else:
                    word_pieces.append('##' + piece)

        # Return the updated tokenized text with prefixes
        return word_pieces