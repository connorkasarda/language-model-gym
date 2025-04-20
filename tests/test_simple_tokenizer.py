"""
name: test_simple_tokenizer.py
Description: Unit tests for the simple tokenizer class.
Author: Connor Kasarda
Date: 2025-04-13

Warning:
    Use at your own risk. The author is not responsible for any damages or losses incurred from using this code.
"""

import unittest
from tokenization.simple_tokenizer import SimpleTokenizer

class TestSimpleTokenizer(unittest.TestCase):
    """
    Test case for the Vocabulary class.

    Attributes:
        simple_tokenizer (Tokenizer): An instance of the Tokenizer class.
    """

    def setUp(self) -> None:
        """
        Set up a Tokenizer for testing.

        Attributes:
            simple_tokenizer (Tokenizer): An instance of the Tokenizer class.
        """

        self.simple_tokenizer = SimpleTokenizer()

    def test_segment(self) -> None:
        """
        Test the tokenize method.

        This test checks if the tokenize method correctly tokenizes a given text.
        """

        text = "Hello, world!"
        expected_tokens = ["Hello", ",", " ", "world", "!"]
        tokens = self.simple_tokenizer.segment(text)
        self.assertEqual(tokens, expected_tokens)

    def test_learn(self) -> None:
        """
        Test the train method.

        Checks if the train function adds tokens to the vocabulary.
        """

        text = 'It\'s a beautiful day!'
        self.simple_tokenizer.learn(text)
        # Remember that we have to compensate for special tokens (normal tokens = 7, special tokens = 4)
        expected_vocab_size = 12
        self.assertEqual(len(self.simple_tokenizer), expected_vocab_size)

    def test_encode(self) -> None:
        """
        Test the encode method.

        This test checks if the encode method correctly encodes a given text.
        """

        text = 'In the beginning, God created the heavens and the earth.'
        self.simple_tokenizer.learn(text)
        actual_token_ids = self.simple_tokenizer.encode(text)
        expected_token_ids = [
            self.simple_tokenizer.vocab.get_id('In'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('the'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('beginning'),
            self.simple_tokenizer.vocab.get_id(','),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('God'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('created'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('the'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('heavens'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('and'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('the'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('earth'),
            self.simple_tokenizer.vocab.get_id('.')
        ]
        self.assertEqual(actual_token_ids, expected_token_ids)

    def test_decode(self) -> None:
        """
        Test the decode method.

        This test checks if the decode method correctly decodes a list of token IDs back to text.
        """

        text = 'The quick brown fox jumps over the lazy dog.'
        self.simple_tokenizer.learn(text)
        token_ids = [
            self.simple_tokenizer.vocab.get_id('The'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('quick'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('brown'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('fox'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('jumps'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('over'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('the'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('lazy'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('dog'),
            self.simple_tokenizer.vocab.get_id('.')
        ]
        actual_decoded_text = self.simple_tokenizer.decode(token_ids)
        expected_decoded_text = 'The quick brown fox jumps over the lazy dog.'
        self.assertEqual(actual_decoded_text, expected_decoded_text)

        unknown_token_ids = [
            self.simple_tokenizer.vocab.get_id('The'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('slow'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('purple'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('elephant'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('falls'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('over'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('the'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('silly'),
            self.simple_tokenizer.vocab.get_id(' '),
            self.simple_tokenizer.vocab.get_id('rat'),
            self.simple_tokenizer.vocab.get_id('!')
        ]
        actual_unknown_decoded_text = self.simple_tokenizer.decode(unknown_token_ids)
        expected_unknown_decoded_text = 'The <UNK> <UNK> <UNK> <UNK> over the <UNK> <UNK><UNK>'
        self.assertEqual(actual_unknown_decoded_text, expected_unknown_decoded_text)
        
if __name__ == '__main__':
    unittest.main()
