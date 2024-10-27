import unittest
from unittest.mock import MagicMock
import random
from database import Hangman


class TestHangman(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hangman = Hangman()
        cls.hangman.load_words()

    def setUp(self):
        self.requested_length = random.randint(6, 10)
        self.hangman.score = 0

    def test_alphabet_count_in_word(self):
        word = "pizza"
        alphabet = 'a'
        count = self.hangman.count_alphabet(word, alphabet)
        self.assertEqual(count, 1)

    def test_length_of_fetched_word_random(self):
        word = self.hangman.fetch_word(self.requested_length)
        self.assertEqual(len(str(word)), self.requested_length)

    def test_uniqueness_of_fetched_word(self):
        used_words = set()
        for _ in range(100):
            word = self.hangman.fetch_word(random.randint(6, 10))
            self.assertTrue(word not in used_words)
            used_words.add(word)

    def test_fetch_clue_before_any_guess(self):
        clue = self.hangman.fetch_clue("pizza")
        self.assertEqual(clue, "-----")

    def test_fetch_clue_after_correct_guess(self):
        clue = self.hangman.fetch_clue("pizza")
        new_clue = self.hangman.fetch_clue_with_guess("pizza", clue, 'a')
        self.assertEqual(new_clue, "----a")

    def test_fetch_clue_after_incorrect_guess(self):
        clue = self.hangman.fetch_clue("pizza")
        new_clue = self.hangman.fetch_clue_with_guess("pizza", clue, 'x')
        self.assertEqual(new_clue, "-----")

    def test_invalid_guess_throws_exception(self):
        with self.assertRaises(ValueError) as context:
            self.hangman.fetch_clue_with_guess("pizza", "-----", '1')
        self.assertEqual(str(context.exception), "Invalid character")

    def test_remaining_trials_before_any_guess(self):
        self.hangman.fetch_word(self.requested_length)
        self.assertEqual(self.hangman.remaining_trials, Hangman.MAX_TRIALS)

    def test_remaining_trials_after_one_guess(self):
        self.hangman.fetch_word(self.requested_length)
        self.hangman.fetch_clue_with_guess("pizza", "-----", 'a')
        self.assertEqual(self.hangman.remaining_trials, Hangman.MAX_TRIALS - 1)

    def test_score_before_any_guess(self):
        self.hangman.fetch_word(self.requested_length)
        self.assertEqual(self.hangman.score, 0)

    def test_score_after_correct_guess(self):
        word = "pizza"
        clue = "-----"
        guess = 'a'
        self.hangman.fetch_clue_with_guess(word, clue, guess)
        self.assertEqual(self.hangman.score, Hangman.MAX_TRIALS / len(word))

    def test_score_after_incorrect_guess(self):
        word = "pizza"
        clue = "-----"
        guess = 'x'
        self.hangman.fetch_clue_with_guess(word, clue, guess)
        self.assertEqual(self.hangman.score, 0)

    def test_save_score_using_mock_db(self):
        mock_score_db = MagicMock()
        hangman = Hangman()
        mock_score_db.write_score_db.return_value = True
        self.assertTrue(hangman.save_word_score("apple", 10, mock_score_db))


if __name__ == '__main__':
    unittest.main()
