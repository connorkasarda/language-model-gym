"""
Name: test_byte_pair_encoding.py
Description: Unit tests for the byte pair encoding (BPE) algorithm.
Author: Connor Kasarda
Date: 2025-04-19

Warning:
    Use at your own risk. The author is not responsible for any damages or losses incurred from using this code.
"""

import unittest
from tokenization.byte_pair_encoding import BytePairEncoding

class TestBytePairEncoding(unittest.TestCase):
    """
    Unit tests for the BytePairEncoding class.
    """

    def setUp(self):
        """
        Set up the test case with a sample vocabulary and BPE instance.
        """
        
        self.byte_pair_encoding = BytePairEncoding()
        self.maxDiff = None

    def test_segment(self):
        """
        Test the segment method of the BytePairEncoding class.
        """
        
        text = "hello, elmo -- I love bacon!"
        expected_tokens = [
            'h', 'el', 'lo', ',', ' ',
            'el', 'm', 'o', ' ', '-', '-', ' ',
            'I', ' ', 'lo', 'v', 'e', ' ',
            'b', 'a', 'c', 'o', 'n', '!'
        ]
        self.byte_pair_encoding.max_num_merges = 2
        tokens = self.byte_pair_encoding.segment(text)
        self.assertEqual(tokens, expected_tokens)

    def test_learn(self):
        """
        Test the learn method of the BytePairEncoding class.
        """    
        
        text = "hello, elmo -- I love bacon!"
        expected_vocab = {
            '<UNK>': 0, '<PAD>': 1, '<BOS>': 2, '<EOS>': 3,
            ' ': 4, '!': 5, ',': 6, '-': 7, 'I': 8, 'a': 9,
            'b': 10, 'c': 11, 'e': 12, 'el': 13, 'h': 14,
            'lo': 15, 'm': 16, 'n': 17, 'o': 18, 'v': 19
        }
        self.byte_pair_encoding.max_num_merges = 2
        self.byte_pair_encoding.learn(text)
        self.assertEqual(self.byte_pair_encoding.vocab.token_2_id_map, expected_vocab)

    def test_encode(self):
        """
        Test the encode method of the BytePairEncoding class.
        """
        
        text_for_training = "hello, elmo -- I love bacon!"
        expected_token_ids = [
            2, 14, 13, 15, 6, 4,
            13, 16, 18, 4, 7, 7, 4,
            8, 4, 15, 19, 12, 4,
            10, 9, 11, 18, 17, 5, 3
        ]
        self.byte_pair_encoding.max_num_merges = 2
        self.byte_pair_encoding.learn(text_for_training)
        text = "<BOS>hello, elmo -- I love bacon!<EOS>"
        actual_token_ids = self.byte_pair_encoding.encode(text)
        self.assertEqual(actual_token_ids, expected_token_ids)

    def test_decode(self):
        """
        Test the decode method of the BytePairEncoding class.
        """
        
        token_ids = [
            2, 14, 13, 15, 6, 4,
            13, 16, 18, 4, 7, 7, 4,
            8, 4, 15, 19, 12, 4,
            10, 9, 11, 18, 17, 5, 3
        ]
        expected_text_for_training = "hello, elmo -- I love bacon!"
        self.byte_pair_encoding.max_num_merges = 2
        self.byte_pair_encoding.learn(expected_text_for_training)
        actual_text = self.byte_pair_encoding.decode(token_ids)
        expected_text = "<BOS>hello, elmo -- I love bacon!<EOS>"
        self.assertEqual(actual_text.strip(), expected_text)