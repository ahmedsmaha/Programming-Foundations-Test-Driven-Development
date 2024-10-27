import unittest
from functionality import Hangman


class TestAddFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hangman = Hangman()

    def test_before_start(self):
        clue = self.hangman.fetch_clue("pizza")
        self.assertEqual(clue, "-----")

    def test_after_correct_start(self):
        clue = self.hangman.fetch_clue_after_guess("pizza", "-----", 'a')
        self.assertEqual(clue, "----a")

    def test_after_wrong_start(self):
        clue = self.hangman.fetch_clue_after_guess("pizza", "-----", 'x')
        self.assertEqual(clue, "-----")


if __name__ == '__main__':
    unittest.main()
