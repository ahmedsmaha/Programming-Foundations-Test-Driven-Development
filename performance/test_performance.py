import unittest
from performance import Hangman


class TestAddFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hangman = Hangman()

    def setUp(self):
        self.hangman.score = 0

    def test_before_guess(self):
        self.hangman.fetch_clue("pizza")
        self.assertEqual(self.hangman.MAX_TRIALS,
                         self.hangman.remaining_trials)

    def test_after_guess(self):
        self.hangman.fetch_clue("pizza")
        self.hangman.fetch_clue_after_guess("pizza", "-----", 'x')
        self.assertEqual(self.hangman.MAX_TRIALS - 1,
                         self.hangman.remaining_trials)

    def test_score_before_guess(self):
        self.hangman.fetch_clue("pizza")
        self.assertEqual(0, self.hangman.score)

    def test_after_correct_guess(self):
        word = "pizza"
        self.hangman.fetch_clue(word)
        self.hangman.fetch_clue_after_guess(word, "-----", 'a')
        self.assertEqual(float(self.hangman.MAX_TRIALS) /
                         len(word), self.hangman.score)

    def test_after_in_correct_guess(self):
        word = "pizza"
        self.hangman.fetch_clue(word)
        self.hangman.fetch_clue_after_guess(word, "-----", 'x')
        self.assertEqual(0, self.hangman.score)


if __name__ == '__main__':
    unittest.main()
