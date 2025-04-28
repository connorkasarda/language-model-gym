"""
Name: test_word_piece.py
Description: Unit tests for the WordPiece tokenizer algorithm
Author: Connor Kasarda
Date: 2025-04-26

Warning:
    Use at your own risk. The author is not responsible for any damages or losses incurred from using this code.
"""

import unittest
import textwrap
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
        expected_vocab = ['<UNK>', '<PAD>', '<BOS>', '<EOS>', ' ', '!', '##er', '##est', 'low']
        actual_vocab = [token for token, _ in self.tokenizer.vocab.token_2_id_map.items()]
        self.assertEqual(actual_vocab, expected_vocab)

    def test_segment(self):
        """
        Test the tokenization of a simple sentence.
        """
        
        text = "low lower lowest!"
        expected_segments = ["low", " ", "low", "##er", " ", "low", "##est", '!']
        actual_segments = self.tokenizer.segment(text)
        self.assertEqual(actual_segments, expected_segments)

    def test_encode_decode(self):
        """
        Test encoding a string to a list of token IDs
        """

        expected_text = textwrap.dedent("""\
                               Hello, and welcome to the Aperture Science Computer-Aided Enrichment Center.
                               We hope your brief detention in the relaxation vault has been a pleasant one.
                               Your specimen has been processed, and we are now ready to begin the test proper.
                               Before we start, however, keep in mind that although fun and learning are the
                               primary goals of all enrichment center activities, serious injuries may occur.
                               For your safety, and the safety of others, please refrain from touching the glass.
                               """)
        self.tokenizer.max_num_merges = 100
        self.tokenizer.learn(expected_text)
        tokenized = self.tokenizer.encode(expected_text)
        actual_text = self.tokenizer.decode(tokenized)
        self.assertEqual(actual_text, expected_text)