class Hangman():

    def fetch_clue(self, word):
        clue = ""
        for i in word:
            clue += '-'
        return clue

    def fetch_clue_after_guess(self, word, clue, char):
        new_clue = ""
        for i, c in enumerate(word):
            if c is char:
                new_clue += c
            else:
                new_clue += clue[i]
        return new_clue
