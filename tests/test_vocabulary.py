"""
name: test_vocabulary.py
Description: Unit tests for the Vocabulary class.
Author: Connor Kasarda
Date: 2025-04-13
"""

import unittest
from tokenization.vocabulary import Vocabulary

class TestVocabulary(unittest.TestCase):
    """
    Test case for the Vocabulary class.

    Attributes:
        vocab (Vocabulary): An instance of the Vocabulary class.
    """

    def setUp(self):
        """
        Set up a Vocabulary instance for testing.

        Attributes:
            vocab (Vocabulary): An instance of the Vocabulary class.
        """

        self.vocab = Vocabulary(max_size=6)

    def test_empty_vocabulary(self):
        """
        Test building an empty vocabulary.
        """

        self.vocab.build()
        self.assertEqual(len(self.vocab), 2)
        self.assertIn('<UNK>', self.vocab.token_2_id_map)
        self.assertIn('<PAD>', self.vocab.token_2_id_map)
        self.assertNotIn('hello', self.vocab.token_2_id_map)

    def test_build_vocabulary(self):
        """
        Test building a vocabulary with tokens.
        """

        tokens = ['hello', 'world', ',', '!']
        self.vocab.build(tokens)
        self.assertEqual(len(self.vocab), 6)
        self.assertIn('hello', self.vocab.token_2_id_map)
        self.assertIn('world', self.vocab.token_2_id_map)
        self.assertIn(',', self.vocab.token_2_id_map)
        self.assertIn('!', self.vocab.token_2_id_map)
        self.assertNotIn('?', self.vocab.token_2_id_map)

    def test_get_id(self):
        """
        Test retrieving token IDs.
        """

        tokens = ['maximum', 'power']
        self.vocab.build(tokens)
        self.assertEqual(self.vocab.get_id('maximum'), self.vocab.token_2_id_map['maximum'])
        self.assertEqual(self.vocab.get_id('power'), self.vocab.token_2_id_map['power'])
        self.assertEqual(self.vocab.get_id(''), self.vocab.UNKNOWN_ID)

    def test_get_token(self):
        """
        Test retrieving tokens by ID.
        """

        tokens = ['apple', 'banana']
        self.vocab.build(tokens)
        self.assertEqual(self.vocab.get_token(self.vocab.token_2_id_map['apple']), 'apple')
        self.assertEqual(self.vocab.get_token(self.vocab.token_2_id_map['banana']), 'banana')
        self.assertEqual(self.vocab.get_token(999), '<UNK>')

    def test_max_size(self):
        """
        Test the maximum size of the vocabulary.
        """

        tokens = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.vocab.build(tokens)
        self.assertEqual(len(self.vocab), 6)

if __name__ == '__main__':
    unittest.main()