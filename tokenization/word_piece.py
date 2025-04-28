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
    Punctuation and whitespace is treated as a special token that cannot be merged with other tokens!

    Attributes:
        vocab (Vocabulary): An instance of the Vocabulary class used for encoding and decoding tokens.
        max_num_merges (int): The maximum number of token-pair merges to perform.

    Methods:
        __init__(): Initializes the WordPiece instance.
        segment(text: str, max_num_merges: int = None) -> list[str]: Tokenizes the input text into a list of tokens using WordPiece.
        encode(text: str) -> list[int]: Encodes the input text into a list of token IDs.
        decode(token_ids: list[int]) -> str: Decodes a list of token IDs back into the original text.
        find_highest_scoring_token_pair(tokenized_text: list[str], token_2_freq_map: dict[str, int]) -> tuple[str, str]: Finds the highest scoring token pair in the tokenized text.
        add_new_token_pair(token_pair: tuple[str, str], token_2_freq_map: dict[str, int], tokenized_text: list[str]) -> list[str]: Adds a new token pair to the tokenized text by merging the highest scoring token pair.
        add_prefixes(tokenized_text: list[str]) -> list[str]: Adds the WordPiece prefix notation (i.e., ##) to the tokenized text where needed.
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

        # Initialize with pre-tokenized text and frequency map, removing whitespaces
        tokenized_text = [char for char in text]
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
        
        # Add prefixes to subwords where necessary
        return self.add_prefixes(tokenized_text)

    def encode(self, text: str) -> list[int]:
        """
        Override of Tokenizer encode method to account for WordPiece prefix notation (i.e., ##).

        Args:
            text (str): The input text to encode.

        Returns:
            list[int]: A list of token IDs corresponding to the input text.
        """

        # Tokenize the text using the WordPiece algorithm
        tokenized_text = self.segment(text)

        # Encode the tokenized text into token IDs
        token_ids = []
        for token in tokenized_text:
            token_id = self.vocab.get_id(token)
            if token_id != self.vocab.UNKNOWN_ID:
                token_ids.append(token_id)
            else:
                token_ids.append(self.vocab.UNKNOWN_ID)

        return token_ids

    def decode(self, token_ids: list[int]) -> str:
        """
        Override of Tokenizer decode method to account for WordPiece prefix notation (i.e., ##).

        Args:
            token_ids (list[int]): A list of token IDs to decode.

        Returns:
            str: The decoded text.
        """

        # Decode the token IDs into tokens
        tokens = [self.vocab.get_token(token_id) for token_id in token_ids]

        # Reconstruct the original text from the tokens but remember to add whitespaces between words and punctuation correctly
        decoded_text = []
        for token in tokens:
            if token.startswith('##'):
                decoded_text[-1] += token[2:]
            else:
                decoded_text.append(token)

        # Combine into a single string
        return ''.join(decoded_text)

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

            # Construct potential token pair
            token_pair = (tokenized_text[token_idx], tokenized_text[token_idx + 1])

            # Skip token pair analysis if either token is punctuation
            if re.fullmatch(r'[^\w\s]|\s', token_pair[0]) or re.fullmatch(r'[^\w\s]|\s', token_pair[1]):
                continue

            # Check if valid token pair is present in the tokenized text
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

        # Skip merging if either token in the pair is punctuation or a whitespace
        if re.fullmatch(r'[^\w\s]|\s', token_pair[0]) or re.fullmatch(r'[^\w\s]|\s', token_pair[1]):
            return tokenized_text

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

    def add_prefixes(self, tokenized_text: list[str]) -> list[str]:
        """
        Adds the WordPiece prefix notation (i.e., ##) to the tokenized text.

        Args:
            tokenized_text (list[str]): The segmented text without prefixes

        Returns:
            list[str]: The updated tokenized text with the WordPiece prefix notation added.
        """

        # Create a list to store the updated tokenized text with prefixes
        prefixed_text = []

        # Variable to track whether the last token was a punctuation or whitespace
        last_was_punctuation_or_whitespace = True

        # Iterate through each token in the tokenized text
        for token in tokenized_text:

            # If the token is punctuation or whitespace, add it as is
            if re.fullmatch(r'[^\w\s]|\s', token):
                prefixed_text.append(token)
                last_was_punctuation_or_whitespace = True

            # We have a subword    
            else:

                # If the last token was punctuation or whitespace, this is the first token of a word
                if last_was_punctuation_or_whitespace:
                    prefixed_text.append(token)
                    last_was_punctuation_or_whitespace = False
                
                # This is a subword, so add the "##" prefix
                else:
                    prefixed_text.append('##' + token)

        # Return the updated tokenized text with prefixes
        return prefixed_text