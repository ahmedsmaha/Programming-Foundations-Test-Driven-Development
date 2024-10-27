class Hangman:
    MAX_TRIALS = 10

    def __init__(self):
        self.used_words_set = set()
        self.words_list = []
        self.remaining_trials = self.MAX_TRIALS
        self.score = 0

    def count_alphabet(self, word, alphabet):
        return word.count(alphabet)

    def fetch_word(self, requested_length):
        self.remaining_trials = self.MAX_TRIALS
        for word in self.words_list:
            if len(word) == requested_length and word not in self.used_words_set:
                self.used_words_set.add(word)
                return word
        return None

    def load_words(self):
        with open("WordSource.txt", "r", encoding="utf-8") as file:
            for line in file:
                self.words_list.append(line.strip())

    def fetch_clue(self, word):
        return '-' * len(word)

    def fetch_clue_with_guess(self, word, clue, guess):
        self.remaining_trials -= 1
        if not guess.isalpha():
            raise ValueError("Invalid character")

        guess = guess.lower()
        new_clue = []
        for i, _ in enumerate(word):
            if guess == word[i] and clue[i] == '-':
                new_clue.append(guess)
                self.score += self.MAX_TRIALS / len(word)
            else:
                new_clue.append(clue[i])
        return ''.join(new_clue)

    def save_word_score(self, word, score, mock_score_db):
        return mock_score_db.write_score_db(word, score)
