"""
Name: test_word_piece.py
Description: Unit tests for the WordPiece tokenizer algorithm
Author: Connor Kasarda
Date: 2025-04-26

Warning:
    Use at your own risk. The author is not responsible for any damages or losses incurred from using this code.
"""

import unittest
from tokenization.word_piece import WordPiece

class TestWordPiece(unittest.TestCase):
    """
    Unit tests for the WordPiece tokenizer algorithm.
    """

    def setUp(self):
        """
        Set up the WordPiece tokenizer for testing.
        """
        self.tokenizer = WordPiece(max_num_merges=5)

    def test_learn(self):
        """
        Test the learning process of the WordPiece tokenizer.
        """
        
        text = "low lower lowest!"
        self.tokenizer.learn(text)
        expected_vocab = ['<UNK>', '<PAD>', '<BOS>', '<EOS>', '!', '##er', '##est', 'low']
        actual_vocab = [token for token, _ in self.tokenizer.vocab.token_2_id_map.items()]
        self.assertEqual(actual_vocab, expected_vocab)

    def test_segment(self):
        """
        Test the tokenization of a simple sentence.
        """
        
        text = "low lower lowest!"
        expected_segments = ["low", "low", "##er", "low", "##est", '!']
        actual_segments = self.tokenizer.segment(text)
        self.assertEqual(actual_segments, expected_segments)

    # encode

    # decode
