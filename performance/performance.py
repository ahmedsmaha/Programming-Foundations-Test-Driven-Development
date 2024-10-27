class Hangman():
    def __init__(self):
        self.MAX_TRIALS = 10
        self.remaining_trials = 0
        self.score = 0

    def fetch_clue(self, word):
        clue = ""
        self.remaining_trials = self.MAX_TRIALS
        for i in word:
            clue += '-'
        return clue

    def fetch_clue_after_guess(self, word, clue, char):
        self.remaining_trials -= 1
        new_clue = ""
        for i, c in enumerate(word):
            if c is char:
                new_clue += c
                self.score += float(self.MAX_TRIALS) / len(word)
            else:
                new_clue += clue[i]
        return new_clue
